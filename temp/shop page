import { Metadata } from 'next';
import Link from 'next/link';
import { getAllCategorySlugs, getCategoryData, getShowcaseProducts } from '@/lib/shop';
import ShopHeroTLDR from '@/components/Shop/ShopHeroTLDR';

// Import main FAQs
async function getMainFAQs() {
  try {
    const faqModule = await import('@/content/shop-faqs/main.json');
    return faqModule.default.faqs || faqModule.faqs || [];
  } catch {
    return [];
  }
}

// Generate FAQ Schema
function generateFAQSchema(faqs: Array<{ question: string; answer: string }>) {
  if (!faqs || faqs.length === 0) return null;

  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  };
}

export const metadata: Metadata = {
  title: 'Press-On Nails 2025: Chrome, Velvet & Trending Designs | Mirelle',
  description: 'Salon-quality press-on nails in 10 minutes. Chrome, velvet & glazed 2025 trends last 7-14 days. Reusable 2-10x, zero damage. Shop 200+ designs from fall to festive.',
  keywords: [
    'press-on nails',
    'press on nails 2025',
    'fake nails',
    'reusable press-on nails',
    'chrome nails',
    'velvet nails',
    'trendy nail designs',
    'salon quality press-ons',
    'best press-on nails',
    'affordable nail art'
  ],
  openGraph: {
    title: 'Press-On Nails 2025: Chrome, Velvet & Trending Designs | Mirellé ',
    description: 'Salon-quality press-on nails that last 7-14 days. 200+ trending designs including chrome, velvet, and seasonal collections. Apply in minutes, reusable 2-10 times.',
    url: 'https://mirelleinspo.com/shop',
    siteName: 'Mirelle',
    locale: 'en_US',
    type: 'website',
    images: [
      {
        url: '/images/shop-hero-press-on-nails.jpg',
        width: 1200,
        height: 630,
        alt: 'Mirelle Press-On Nails Collection 2025 - Chrome, Velvet and Trendy Designs'
      }
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Press-On Nails 2025: Chrome, Velvet & Trending Designs',
    description: 'Salon-quality press-on nails in 10 minutes. 200+ designs, lasts 2 weeks, reusable.',
    images: ['/images/shop-hero-press-on-nails.jpg'],
  },
  alternates: {
    canonical: 'https://mirelleinspo.com/shop',
  },
}

export default async function ShopPage() {
  const categorySlugs = getAllCategorySlugs();
  const categories = categorySlugs.map(slug => getCategoryData(slug)).filter(Boolean);
  
  // Get showcase products and FAQs
  const showcaseProducts = await getShowcaseProducts();
  const showcaseImages = showcaseProducts.map(p => p.image);
  const faqs = await getMainFAQs();
  
  const faqSchema = generateFAQSchema(faqs);

  // Category hero images mapping (using showcase images)
  const categoryHeroImages: { [key: string]: string } = {
    'fall': showcaseImages[0] || '/fallsection.jpg',
    'christmas': showcaseImages[1] || '/christmassection.jpg',
    'winter': showcaseImages[2] || '/wintersection.jpg',
    'halloween': showcaseImages[3] || '/halloweenbannerimg.jpg',
    'new-year': showcaseImages[4] || '/newyearsection.jpeg',
    'trendy': showcaseImages[5] || '/trendsection.jpg',
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* FAQ Schema */}
      {faqSchema && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(faqSchema),
          }}
        />
      )}

      {/* Hero TL;DR Section */}
      <ShopHeroTLDR showcaseImages={showcaseImages} faqs={faqs} />

      {/* Categories Grid */}
      <section id="categories-section" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h2 className="text-3xl font-bold text-gray-900 mb-12 text-center">
          Browse Collections
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {categories.map((category) => {
            if (!category) return null;
            
            // Use showcase image or fallback
            const categoryImage = categoryHeroImages[category.slug] || category.heroImage;
            
            return (
              <Link
                key={category.slug}
                href={`/shop/${category.slug}`}
                className="group relative bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden"
              >
                {/* Category Image */}
                <div className="relative h-80 overflow-hidden">
                  <div
                    className="absolute inset-0 bg-cover bg-center transform group-hover:scale-110 transition-transform duration-500"
                    style={{ backgroundImage: `url(${categoryImage})` }}
                  />
                  {/* Premium gradient overlay */}
                  <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent group-hover:from-black/70 transition-all duration-500" />
                  
                  {/* Category Info Overlay */}
                  <div className="absolute bottom-0 left-0 right-0 p-6 text-white">
                    <h3 className="text-2xl font-bold mb-2 group-hover:text-purple-300 transition-colors">
                      {category.displayName}
                    </h3>
                    <p className="text-white/90 mb-4 text-sm">
                      {category.description}
                    </p>
                    <div className="inline-flex items-center text-white font-semibold border-b-2 border-transparent group-hover:border-purple-300 transition-all">
                      Shop Now
                      <svg className="w-5 h-5 ml-2 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                      </svg>
                    </div>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      {/* Features Section */}
      <section className="bg-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-12 text-center">
            Why Shop With Us?
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Premium Quality</h3>
              <p className="text-gray-600">Handpicked designs that last and look amazing</p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-pink-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-pink-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Affordable Prices</h3>
              <p className="text-gray-600">Starting at just $3.99 with free shipping</p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Fast Delivery</h3>
              <p className="text-gray-600">Quick shipping so you can rock your new nails ASAP</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
