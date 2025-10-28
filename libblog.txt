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

export async function getAllBlogPosts(): Promise<BlogMetadata[]> {
  try {
    const files = fs.readdirSync(BLOG_DIRECTORY);
    const posts = files
      .filter(file => file.endsWith('.md'))
      .map(file => {
        const slug = file.replace('.md', '');
        const filePath = path.join(BLOG_DIRECTORY, file);
        const content = fs.readFileSync(filePath, 'utf8');
        const { data } = matter(content);
        
        return {
          slug,
          title: data.title || 'Untitled',
          excerpt: data.excerpt || '',
          date: data.date || new Date().toISOString(),
          author: data.author || 'Anonymous',
          tags: data.tags || [],
          image: data.image || null,
          readTime: data.readTime || '5 min',
          canonical: data.canonical || `https://mirelleinspo.com/blog/${slug}`,
          faqItems: data.faqItems || undefined, // REMOVE - Not needed in metadata
          tutorialSteps: data.tutorialSteps || undefined, // REMOVE - Not needed in metadata
          tutorialMetadata: data.tutorialMetadata || undefined, // REMOVE - Not needed in metadata
          imageAlt: data.imageAlt || undefined, // NEW ADDED - For generator compatibility
          category: data.category || undefined, // NEW ADDED - For article section
        };
      })
      .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
    return posts;
  } catch (error) {
    console.error('Error reading blog posts:', error);
    return [];
  }
}

export async function getBlogPost(slug: string): Promise<BlogPost | null> {
  try {
    const filePath = path.join(BLOG_DIRECTORY, `${slug}.md`);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const { data, content: markdownContent } = matter(fileContent);
    
    // Convert markdown to HTML
    let htmlContent = await marked(markdownContent);
    
    // Add IDs to H2 headings using regex (simpler approach)
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

    // ✨ NEW - Extract TL;DR from frontmatter
    const tldr = data.tldr
      ? {
          summary: data.tldr.summary || [],
          keyTakeaways: data.tldr.keyTakeaways || []
        }
      : undefined;
    
    return {
      slug,
      title: data.title || 'Untitled',
      excerpt: data.excerpt || '',
      content: htmlContent,
      date: data.date || new Date().toISOString(),
      author: data.author || 'Anonymous',
      tags: data.tags || [],
      image: data.image || null,
      readTime: data.readTime || '5 min',
      canonical: data.canonical || `https://mirelleinspo.com/blog/${slug}`,
      updatedDate: data.updatedDate || undefined, // NEW ADDED - For last modified date
      category: data.category || undefined, // NEW ADDED - For article section
      imageAlt: data.imageAlt || undefined, // NEW ADDED - For image alt text from generator
      imageWidth: data.imageWidth || undefined, // NEW ADDED - For image width from generator
      imageHeight: data.imageHeight || undefined, // NEW ADDED - For image height from generator
      dateModified: data.dateModified || data.updatedDate || undefined, // NEW ADDED - For generator's dateModified field
      wordCount: data.wordCount || undefined, // NEW ADDED - For generator's word count
      faqItems: data.faqItems || undefined,
      tutorialSteps: data.tutorialSteps || undefined,
      tutorialMetadata: data.tutorialMetadata || undefined,
      videoMetadata: data.videoMetadata || undefined,
      tldr, // ✅ NEW FIELD INCLUDED HERE
    };
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
