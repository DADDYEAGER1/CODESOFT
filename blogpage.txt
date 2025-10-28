import { Metadata } from 'next';
import { getAllBlogPosts } from '@/lib/blog';
import BlogCard from '@/components/Blog/BlogCard';
import { generateBlogSchema, generateBlogListSchema } from '@/lib/generateSchemas';

// SEO-Optimized Metadata
export const metadata: Metadata = {
  title: 'Nail Care Blog - Expert Tips, Trends & Tutorials | Mirelle',
  description: 'Discover 100+ expert nail care articles, seasonal trends, step-by-step tutorials, and professional manicure tips. Your ultimate guide to beautiful, healthy nails.',
  keywords: 'nail care blog, nail tips 2025, nail trends, nail art tutorials, manicure tips, nail health, professional nail care, seasonal nail designs, nail inspiration, beauty blog',
  authors: [{ name: 'Mirelle' }],
  creator: 'Mirelle',
  publisher: 'Mirelle',
  alternates: {
    canonical: 'https://mirelleinspo.com/blog',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  openGraph: {
    title: 'Nail Care Blog - Expert Tips, Trends & Tutorials | Mirelle',
    description: 'Discover expert nail care articles, seasonal trends, and step-by-step tutorials. Your ultimate guide to beautiful, healthy nails.',
    type: 'website',
    url: 'https://mirelleinspo.com/blog',
    siteName: 'Mirelle',
    locale: 'en_US',
    images: [{
      url: 'https://mirelleinspo.com/blog-hero.jpg',
      width: 1200,
      height: 630,
      alt: 'Mirelle Nail Care Blog',
      type: 'image/jpeg',
    }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Nail Care Blog | Mirelle',
    description: 'Expert nail care articles, trends & tutorials',
    images: ['https://mirelleinspo.com/blog-hero.jpg'],
    creator: '@mirelleinspo',
    site: '@mirelleinspo',
  },
};

export default async function BlogPage() {
  const posts = await getAllBlogPosts();
  const baseUrl = 'https://mirelleinspo.com';

  // Generate enhanced schemas using lib functions
  const blogSchema = generateBlogSchema();
  const itemListSchema = generateBlogListSchema(posts);

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'Home',
        item: 'https://mirelleinspo.com',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: 'Blog',
        item: 'https://mirelleinspo.com/blog',
      },
    ],
  };

  return (
    <>
      {/* Enhanced Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(blogSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(itemListSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
      />

      <div className="min-h-screen">
        {/* Hero Section */}
        <section className="relative bg-gradient-to-r from-pink-200 to-purple-200 py-20">
          <div className="container mx-auto px-4 text-center">
            <h1 className="text-5xl font-bold text-gray-800 mb-4">
              Nail Care Blog - Expert Tips & Trends
            </h1>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Discover professional nail care advice, seasonal trends, and step-by-step tutorials for beautiful, healthy nails
            </p>
            
            {/* Trust Signals */}
            <div className="flex flex-wrap justify-center gap-6 mt-8">
              <div className="flex items-center gap-2 text-gray-700">
                <span className="text-2xl">📝</span>
                <span className="font-semibold">{posts.length}+ Articles</span>
              </div>
              <div className="flex items-center gap-2 text-gray-700">
                <span className="text-2xl">✨</span>
                <span className="font-semibold">Expert Advice</span>
              </div>
              <div className="flex items-center gap-2 text-gray-700">
                <span className="text-2xl">📆</span>
                <span className="font-semibold">Updated Weekly</span>
              </div>
            </div>
          </div>
        </section>

        {/* Blog Grid Section */}
        <section className="py-16 bg-white">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-gray-800 mb-4">
                Latest Nail Care Articles
              </h2>
              <p className="text-gray-600 max-w-2xl mx-auto">
                From nail care basics to advanced techniques, explore everything you need to know about achieving salon-quality nails at home
              </p>
            </div>

            {posts.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {posts.map((post) => (
                  <BlogCard key={post.slug} post={post} />
                ))}
              </div>
            ) : (
              <div className="text-center py-16">
                <h3 className="text-2xl font-bold text-gray-600 mb-4">
                  Amazing Content Coming Soon
                </h3>
                <p className="text-gray-500">
                  We're crafting expert nail care content for you. Check back soon!
                </p>
              </div>
            )}
          </div>
        </section>

        {/* Categories Section for Internal Linking */}
        <section className="py-16 bg-gray-50">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">
              Popular Topics
            </h2>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              {[
                { name: 'Nail Care', icon: '💅' },
                { name: 'Nail Art', icon: '🎨' },
                { name: 'Seasonal Trends', icon: '🍂' },
                { name: 'Tutorials', icon: '📚' },
              ].map((topic) => (
                <div
                  key={topic.name}
                  className="bg-white p-6 rounded-lg text-center hover:shadow-lg transition-shadow"
                >
                  <div className="text-4xl mb-2">{topic.icon}</div>
                  <h3 className="font-semibold text-gray-800">{topic.name}</h3>
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </>
  );
}
