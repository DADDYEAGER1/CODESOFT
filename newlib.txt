import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { BlogPost, BlogMetadata } from '@/types/blog';
import { marked } from 'marked';

marked.setOptions({
  breaks: true,
  gfm: true,
});

const BLOG_DIRECTORY = path.join(process.cwd(), 'src/content/blogs');
const METADATA_DIRECTORY = path.join(process.cwd(), 'src/content/metadata');

// ✅ NEW - In-memory cache for metadata
interface CacheEntry<T> {
  data: T;
  timestamp: number;
}

class MetadataCache {
  private cache = new Map<string, CacheEntry<any>>();
  private readonly TTL = 3600000; // 1 hour in milliseconds

  get<T>(key: string): T | null {
    const entry = this.cache.get(key);
    if (!entry) return null;

    // Check if cache is expired
    if (Date.now() - entry.timestamp > this.TTL) {
      this.cache.delete(key);
      return null;
    }

    return entry.data as T;
  }

  set<T>(key: string, data: T): void {
    this.cache.set(key, {
      data,
      timestamp: Date.now(),
    });
  }

  clear(): void {
    this.cache.clear();
  }

  // Get cache statistics
  getStats() {
    return {
      size: this.cache.size,
      keys: Array.from(this.cache.keys()),
    };
  }
}

// ✅ NEW - Global cache instance
const metadataCache = new MetadataCache();

// ✅ NEW - Helper to load metadata files with caching
function loadMetadataFile<T>(filename: string): T {
  const cacheKey = `metadata:${filename}`;
  
  // Try to get from cache first
  const cached = metadataCache.get<T>(cacheKey);
  if (cached) {
    return cached;
  }

  // Load from file system
  try {
    const filePath = path.join(METADATA_DIRECTORY, filename);
    const content = fs.readFileSync(filePath, 'utf8');
    const data = JSON.parse(content) as T;
    
    // Store in cache
    metadataCache.set(cacheKey, data);
    
    return data;
  } catch (error) {
    console.error(`Error loading metadata file ${filename}:`, error);
    return {} as T;
  }
}

// ✅ NEW - Get metadata from JSON files
function getMetadataFromJSON(slug: string): Partial<BlogMetadata> {
  try {
    const titles = loadMetadataFile<Record<string, string>>('titles.json');
    const excerpts = loadMetadataFile<Record<string, string>>('excerpts.json');
    const tags = loadMetadataFile<Record<string, string[]>>('tags.json');
    const images = loadMetadataFile<Record<string, string>>('images.json');
    const imageAlts = loadMetadataFile<Record<string, string>>('imageAlts.json');
    const dateModified = loadMetadataFile<Record<string, string>>('dateModified.json');
    const tldrs = loadMetadataFile<Record<string, string>>('tldr.json');
    const faqs = loadMetadataFile<Record<string, any[]>>('faqItems.json');

    return {
      title: titles[slug],
      excerpt: excerpts[slug],
      tags: tags[slug],
      image: images[slug],
      imageAlt: imageAlts[slug],
      dateModified: dateModified[slug],
      tldr: tldrs[slug],
      faqItems: faqs[slug],
    };
  } catch (error) {
    console.error(`Error getting metadata for ${slug}:`, error);
    return {};
  }
}

// ✅ NEW - Get core metadata from frontmatter
function getMetadataFromFrontmatter(slug: string): Partial<BlogMetadata> {
  try {
    const filePath = path.join(BLOG_DIRECTORY, `${slug}.md`);
    const content = fs.readFileSync(filePath, 'utf8');
    const { data } = matter(content);
    
    return {
      date: data.date,
      author: data.author,
      readTime: data.readTime,
      category: data.category,
      canonical: data.canonical || `https://mirelleinspo.com/blog/${slug}`,
      tutorialSteps: data.tutorialSteps,
      tutorialMetadata: data.tutorialMetadata,
      galleryImages: data.galleryImages,
    };
  } catch (error) {
    console.error(`Error reading frontmatter for ${slug}:`, error);
    return {};
  }
}

// 🔄 UPDATED - getAllBlogPosts with caching
export async function getAllBlogPosts(): Promise<BlogMetadata[]> {
  const cacheKey = 'all-blog-posts';
  
  // Try cache first
  const cached = metadataCache.get<BlogMetadata[]>(cacheKey);
  if (cached) {
    return cached;
  }

  try {
    const files = fs.readdirSync(BLOG_DIRECTORY);
    const posts = files
      .filter(file => file.endsWith('.md'))
      .map(file => {
        const slug = file.replace('.md', '');
        
        // ✅ NEW - Merge JSON metadata with frontmatter
        const jsonMetadata = getMetadataFromJSON(slug);
        const frontmatterMetadata = getMetadataFromFrontmatter(slug);
        
        return {
          slug,
          title: jsonMetadata.title || 'Untitled',
          excerpt: jsonMetadata.excerpt || '',
          date: frontmatterMetadata.date || new Date().toISOString(),
          author: frontmatterMetadata.author || 'Anonymous',
          tags: jsonMetadata.tags || [],
          image: jsonMetadata.image || null,
          imageAlt: jsonMetadata.imageAlt,
          readTime: frontmatterMetadata.readTime || '5 min',
          category: frontmatterMetadata.category,
          canonical: frontmatterMetadata.canonical || `https://mirelleinspo.com/blog/${slug}`,
          dateModified: jsonMetadata.dateModified,
          tldr: jsonMetadata.tldr,
          faqItems: jsonMetadata.faqItems,
          tutorialSteps: frontmatterMetadata.tutorialSteps,
          tutorialMetadata: frontmatterMetadata.tutorialMetadata,
          galleryImages: frontmatterMetadata.galleryImages,
        } as BlogMetadata;
      })
      .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
    
    // Store in cache
    metadataCache.set(cacheKey, posts);
    
    return posts;
  } catch (error) {
    console.error('Error reading blog posts:', error);
    return [];
  }
}

// 🔄 UPDATED - getBlogPost with caching
export async function getBlogPost(slug: string): Promise<BlogPost | null> {
  const cacheKey = `blog-post:${slug}`;
  
  // Try cache first
  const cached = metadataCache.get<BlogPost>(cacheKey);
  if (cached) {
    return cached;
  }

  try {
    const filePath = path.join(BLOG_DIRECTORY, `${slug}.md`);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const { data, content: markdownContent } = matter(fileContent);
    
    // Convert markdown to HTML
    let htmlContent = await marked(markdownContent);
    
    // Add IDs to H2 headings using regex
    htmlContent = htmlContent.replace(
      /<h2>(.*?)<\/h2>/g,
      (match, text) => {
        const cleanText = text.replace(/<[^>]*>/g, '');
        const id = cleanText
          .toLowerCase()
          .replace(/[^a-z0-9]+/g, '-')
          .replace(/^-+|-+$/g, '');
        return `<h2 id="${id}">${text}</h2>`;
      }
    );
    
    // ✅ NEW - Merge JSON metadata
    const jsonMetadata = getMetadataFromJSON(slug);
    
    const post: BlogPost = {
      slug,
      title: jsonMetadata.title || data.title || 'Untitled',
      excerpt: jsonMetadata.excerpt || data.excerpt || '',
      content: htmlContent,
      date: data.date || new Date().toISOString(),
      author: data.author || 'Anonymous',
      tags: jsonMetadata.tags || data.tags || [],
      image: jsonMetadata.image || data.image || null,
      imageAlt: jsonMetadata.imageAlt || data.imageAlt,
      readTime: data.readTime || '5 min',
      category: data.category,
      canonical: data.canonical || `https://mirelleinspo.com/blog/${slug}`,
      dateModified: jsonMetadata.dateModified || data.dateModified,
      tldr: jsonMetadata.tldr || data.tldr,
      faqItems: jsonMetadata.faqItems || data.faqItems,
      tutorialSteps: data.tutorialSteps,
      tutorialMetadata: data.tutorialMetadata,
      galleryImages: data.galleryImages,
    };
    
    // Store in cache
    metadataCache.set(cacheKey, post);
    
    return post;
  } catch (error) {
    console.error(`Error reading blog post ${slug}:`, error);
    return null;
  }
}

export async function getAllBlogSlugs(): Promise<string[]> {
  try {
    const files = fs.readdirSync(BLOG_DIRECTORY);
    return files
      .filter(file => file.endsWith('.md'))
      .map(file => file.replace('.md', ''));
  } catch (error) {
    console.error('Error reading blog slugs:', error);
    return [];
  }
}

// ✅ NEW - Get posts by category with caching
export async function getPostsByCategory(category: string): Promise<BlogMetadata[]> {
  const cacheKey = `category:${category}`;
  
  const cached = metadataCache.get<BlogMetadata[]>(cacheKey);
  if (cached) return cached;

  const allPosts = await getAllBlogPosts();
  const filtered = allPosts.filter(post => post.category === category);
  
  metadataCache.set(cacheKey, filtered);
  return filtered;
}

// ✅ NEW - Get posts by tag with caching
export async function getPostsByTag(tag: string): Promise<BlogMetadata[]> {
  const cacheKey = `tag:${tag}`;
  
  const cached = metadataCache.get<BlogMetadata[]>(cacheKey);
  if (cached) return cached;

  const allPosts = await getAllBlogPosts();
  const filtered = allPosts.filter(post => 
    post.tags?.some(t => t.toLowerCase() === tag.toLowerCase())
  );
  
  metadataCache.set(cacheKey, filtered);
  return filtered;
}

// ✅ NEW - Get all categories
export async function getAllCategories() {
  const allPosts = await getAllBlogPosts();
  const categoryMap = new Map<string, number>();
  
  allPosts.forEach(post => {
    if (post.category) {
      categoryMap.set(post.category, (categoryMap.get(post.category) || 0) + 1);
    }
  });
  
  return Array.from(categoryMap.entries()).map(([name, count]) => ({
    name,
    slug: name.toLowerCase().replace(/\s+/g, '-'),
    count,
  }));
}

// ✅ NEW - Get all tags
export async function getAllTags() {
  const allPosts = await getAllBlogPosts();
  const tagMap = new Map<string, number>();
  
  allPosts.forEach(post => {
    post.tags?.forEach(tag => {
      tagMap.set(tag, (tagMap.get(tag) || 0) + 1);
    });
  });
  
  return Array.from(tagMap.entries())
    .map(([name, count]) => ({
      name,
      slug: name.toLowerCase().replace(/\s+/g, '-'),
      count,
    }))
    .sort((a, b) => b.count - a.count);
}

// ✅ NEW - Get related posts
export async function getRelatedPosts(currentSlug: string, limit: number = 3): Promise<BlogMetadata[]> {
  const currentPost = await getBlogPost(currentSlug);
  if (!currentPost) return [];
  
  const allPosts = await getAllBlogPosts();
  
  // Score posts by relevance
  const scoredPosts = allPosts
    .filter(post => post.slug !== currentSlug)
    .map(post => {
      let score = 0;
      
      // Same category = +3 points
      if (post.category === currentPost.category) score += 3;
      
      // Shared tags = +1 point per tag
      const sharedTags = post.tags?.filter(tag => 
        currentPost.tags?.includes(tag)
      ).length || 0;
      score += sharedTags;
      
      return { post, score };
    })
    .filter(item => item.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit)
    .map(item => item.post);
  
  return scoredPosts;
}

// ✅ NEW - Get paginated posts
export async function getPaginatedPosts(page: number = 1, perPage: number = 12): Promise<{
  posts: BlogMetadata[];
  totalPages: number;
  currentPage: number;
  totalPosts: number;
}> {
  const allPosts = await getAllBlogPosts();
  const totalPosts = allPosts.length;
  const totalPages = Math.ceil(totalPosts / perPage);
  const startIndex = (page - 1) * perPage;
  const endIndex = startIndex + perPage;
  const posts = allPosts.slice(startIndex, endIndex);
  
  return {
    posts,
    totalPages,
    currentPage: page,
    totalPosts,
  };
}

// ✅ NEW - Clear cache (useful for development)
export function clearBlogCache() {
  metadataCache.clear();
}

// ✅ NEW - Get cache stats (useful for debugging)
export function getCacheStats() {
  return metadataCache.getStats();
}
