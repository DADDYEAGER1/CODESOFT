import { Metadata } from 'next';
import Link from 'next/link';
import { getAllCategorySlugs, getCategoryData } from '@/lib/shop';

export const metadata: Metadata = {
  title: 'Shop Press-On Nails - All Collections | Mirelle',
  description: 'Browse our complete collection of press-on nails. Find fall, winter, Christmas, Halloween, New Year, and trendy nail designs.',
  keywords: 'press-on nails, fake nails, nail art, seasonal nails, trendy nails',
  openGraph: {
    title: 'Shop Press-On Nails - All Collections | Mirelle',
    description: 'Browse our complete collection of press-on nails.',
    url: 'https://mirelleinspo.com/shop',
    siteName: 'Mirelle',
    locale: 'en_US',
    type: 'website',
  },
  alternates: {
    canonical: 'https://mirelleinspo.com/shop',
  },
};

export default function ShopPage() {
  const categorySlugs = getAllCategorySlugs();
  const categories = categorySlugs.map(slug => getCategoryData(slug)).filter(Boolean);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-pink-600 via-purple-600 to-blue-600 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Shop Press-On Nails
          </h1>
          <p className="text-xl md:text-2xl text-white/90 max-w-3xl mx-auto">
            Discover our curated collection of premium press-on nails for every season and style
          </p>
        </div>
      </section>

      {/* Categories Grid */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h2 className="text-3xl font-bold text-gray-900 mb-12 text-center">
          Browse Collections
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {categories.map((category) => {
            if (!category) return null;
            
            return (
              <Link
                key={category.slug}
                href={`/shop/${category.slug}`}
                className="group relative bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden"
              >
                {/* Category Image */}
                <div className="relative h-64 overflow-hidden">
                  <div
                    className="absolute inset-0 bg-cover bg-center transform group-hover:scale-110 transition-transform duration-300"
                    style={{ backgroundImage: `url(${category.heroImage})` }}
                  />
                  <div className={`absolute inset-0 bg-gradient-to-r from-${category.gradientFrom} via-${category.gradientVia} to-${category.gradientTo} opacity-60 group-hover:opacity-40 transition-opacity`} />
                  
                  {/* Emojis */}
                  <div className="absolute inset-0 flex items-center justify-center gap-4 text-5xl">
                    {category.emojis.slice(0, 3).map((emoji, i) => (
                      <span key={i} className="drop-shadow-lg">
                        {emoji}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Category Info */}
                <div className="p-6">
                  <h3 className="text-2xl font-bold text-gray-900 mb-2 group-hover:text-purple-600 transition-colors">
                    {category.displayName}
                  </h3>
                  <p className="text-gray-600 mb-4">
                    {category.description}
                  </p>
                  <div className="flex items-center text-purple-600 font-semibold">
                    Shop Now
                    <svg className="w-5 h-5 ml-2 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
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
