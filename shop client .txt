// src/components/Shop/ShopClient.tsx
// FIXED VERSION - Matches all type definitions

'use client';


import { useState } from 'react';
import Link from 'next/link';
import { ArrowLeft, ChevronDown, ChevronUp } from 'lucide-react';
import type { CategoryData, Product } from '@/types/shop';
import { calculateDiscount } from '@/lib/shop';

interface ShopClientProps {
  categoryData: CategoryData;
  initialProducts: Product[];
  tldr?: {
    summary: string[];
    keyTakeaways?: string[];
  };
  faqs?: Array<{ question: string; answer: string; keywords?: string[] }>;
  description?: {
    html: string;
    perfectFor?: string[];
  } | null;
}

{tldr && (
  <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div className="bg-gradient-to-br from-pink-50 to-purple-50 border-l-4 border-pink-500 p-6 rounded-lg shadow-md">
      <div className="flex items-center gap-2 mb-4">
        <span className="text-2xl">⚡</span>
        <h2 className="text-xl font-bold text-gray-900 font-serif">Quick Collection Overview</h2>
      </div>
      
      <div className="space-y-3">
        <ul className="space-y-2">
          {tldr.summary.map((item, index) => (
            <li key={index} className="flex items-start gap-2">
              <span className="text-pink-500 mt-1">✓</span>
              <span className="text-gray-700">{item}</span>
            </li>
          ))}
        </ul>
        
        {tldr.keyTakeaways && tldr.keyTakeaways.length > 0 && (
          <div className="mt-4 pt-4 border-t border-pink-200">
            <p className="text-gray-700 font-medium mb-2">Key Features:</p>
            <div className="flex flex-wrap gap-2">
              {tldr.keyTakeaways.map((takeaway, index) => (
                <span 
                  key={index} 
                  className="bg-pink-100 text-pink-700 px-3 py-1 rounded-full text-sm font-medium"
                >
                  {takeaway}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  </section>
)}

export default function ShopClient({
  categoryData,
  initialProducts,
  faqs = [],
  description = null,
}: ShopClientProps) {
  const [filter, setFilter] = useState<'all' | 'new' | 'trending' | 'sale'>('all');
  const [showAll, setShowAll] = useState(false);
  const [openFaqIndex, setOpenFaqIndex] = useState<number | null>(null);

  // Filter products - FIXED: use originalPrice vs price for sale detection
  const filteredProducts = initialProducts.filter((product) => {
    if (filter === 'all') return true;
    if (filter === 'new') return product.isNew;
    if (filter === 'trending') return product.isTrending;
    if (filter === 'sale') return product.originalPrice !== product.price;
    return true;
  });

  // Display products (15 initially, then all)
  const displayProducts = showAll
    ? filteredProducts
    : filteredProducts.slice(0, 15);

  const hasMore = filteredProducts.length > 15 && !showAll;

  // Toggle FAQ accordion
  const toggleFaq = (index: number) => {
    setOpenFaqIndex(openFaqIndex === index ? null : index);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-white">
      {/* Back Button */}
      <div className="max-w-7xl mx-auto px-4 pt-6">
        <Link
          href="/shop"
          className="inline-flex items-center text-gray-600 hover:text-gray-900 transition-colors"
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to Shop
        </Link>
      </div>

      {/* Hero Section - FIXED: Use categoryData properties directly */}
      <section className="relative overflow-hidden">
        <div
          className={`absolute inset-0 bg-gradient-to-br from-${categoryData.gradientFrom} via-${categoryData.gradientVia} to-${categoryData.gradientTo} opacity-90`}
        />
        <div className="relative max-w-7xl mx-auto px-4 py-16 sm:py-24">
          <div className="text-center">
            {/* Floating Emojis - FIXED: Use categoryData.emojis */}
            {categoryData.emojis && categoryData.emojis.length > 0 && (
              <div className="absolute inset-0 pointer-events-none">
                {categoryData.emojis.map((emoji, i) => (
                  <span
                    key={i}
                    className="absolute text-4xl sm:text-6xl opacity-20 animate-float"
                    style={{
                      left: `${(i * 25) % 100}%`,
                      top: `${(i * 30) % 100}%`,
                      animationDelay: `${i * 0.5}s`,
                    }}
                  >
                    {emoji}
                  </span>
                ))}
              </div>
            )}

            {/* FIXED: Use displayName and year */}
            <h1 className="text-5xl sm:text-6xl font-bold text-white mb-6 drop-shadow-lg">
              {categoryData.displayName} {categoryData.year}
            </h1>
            <p className="text-xl sm:text-2xl text-white/90 max-w-3xl mx-auto drop-shadow-md">
              {categoryData.description}
            </p>
          </div>
        </div>
      </section>

      {/* SEO Description Section */}
      {description && (
        <section className="max-w-4xl mx-auto px-4 py-12">
          <div className="prose prose-lg max-w-none">
            <div
              dangerouslySetInnerHTML={{ __html: description.html }}
              className="text-gray-700 leading-relaxed"
            />
            {description.perfectFor && description.perfectFor.length > 0 && (
              <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-100">
                <p className="font-semibold text-gray-900 mb-2">Perfect for:</p>
                <p className="text-gray-700 text-sm">
                  {description.perfectFor.join(', ')}
                </p>
              </div>
            )}
          </div>
        </section>
      )}

      {/* Filter Bar */}
      <section className="max-w-7xl mx-auto px-4 py-8">
        <div className="flex flex-wrap gap-3 justify-center">
          {[
            { key: 'all', label: 'All Products' },
            { key: 'new', label: 'New Arrivals' },
            { key: 'trending', label: 'Trending' },
            { key: 'sale', label: 'On Sale' },
          ].map((item) => (
            <button
              key={item.key}
              onClick={() => setFilter(item.key as any)}
              className={`px-6 py-2.5 rounded-full font-medium transition-all ${
                filter === item.key
                  ? 'bg-gray-900 text-white shadow-lg scale-105'
                  : 'bg-white text-gray-700 hover:bg-gray-100 shadow'
              }`}
            >
              {item.label}
            </button>
          ))}
        </div>
        <p className="text-center mt-4 text-gray-600">
          Showing {displayProducts.length} of {filteredProducts.length} products
        </p>
      </section>

      {/* Products Grid */}
      <section className="max-w-7xl mx-auto px-4 pb-12">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {displayProducts.map((product) => {
            // FIXED: Use calculateDiscount with string prices
            const discount = calculateDiscount(product.originalPrice, product.price);

            return (
              <a
                key={product.id}
                href={product.affiliateUrl} // FIXED: Changed from affiliateLink
                target="_blank"
                rel="noopener noreferrer sponsored"
                className="group bg-white rounded-xl shadow-md hover:shadow-2xl transition-all duration-300 overflow-hidden"
              >
                {/* Product Image */}
                <div className="relative aspect-square overflow-hidden bg-gray-100">
                  <img
                    src={product.image}
                    alt={product.description || product.name} // FIXED: Added fallback
                    className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
                  />
                  {/* Badges */}
                  <div className="absolute top-2 left-2 flex flex-col gap-1">
                    {product.isNew && (
                      <span className="px-2 py-1 bg-blue-500 text-white text-xs font-bold rounded">
                        NEW
                      </span>
                    )}
                    {product.isTrending && (
                      <span className="px-2 py-1 bg-purple-500 text-white text-xs font-bold rounded">
                        TRENDING
                      </span>
                    )}
                    {/* FIXED: Added stockStatus badge */}
                    {product.stockStatus === 'low-stock' && (
                      <span className="px-2 py-1 bg-orange-500 text-white text-xs font-bold rounded">
                        LOW STOCK
                      </span>
                    )}
                    {discount > 0 && (
                      <span className="px-2 py-1 bg-red-500 text-white text-xs font-bold rounded">
                        {discount}% OFF
                      </span>
                    )}
                  </div>
                </div>

                {/* Product Info */}
                <div className="p-4">
                  <h3 className="font-semibold text-gray-900 mb-2 line-clamp-2 group-hover:text-blue-600 transition-colors">
                    {product.name}
                  </h3>
                  {/* FIXED: Use originalPrice vs price comparison */}
                  <div className="flex items-center gap-2">
                    {product.originalPrice !== product.price ? (
                      <>
                        <span className="text-xl font-bold text-red-600">
                          {product.price}
                        </span>
                        <span className="text-sm text-gray-500 line-through">
                          {product.originalPrice}
                        </span>
                      </>
                    ) : (
                      <span className="text-xl font-bold text-gray-900">
                        {product.price}
                      </span>
                    )}
                  </div>
                  {product.rating && (
                    <div className="flex items-center gap-1 mt-2">
                      <span className="text-yellow-500">★</span>
                      <span className="text-sm text-gray-600">{product.rating}</span>
                    </div>
                  )}
                  {/* FIXED: Added CTA button */}
                  <button className="mt-3 w-full bg-gray-900 text-white py-2 rounded-lg font-medium hover:bg-gray-800 transition-colors">
                    {product.cta}
                  </button>
                </div>
              </a>
            );
          })}
        </div>

        {/* Load More Button */}
        {hasMore && (
          <div className="text-center mt-10">
            <button
              onClick={() => setShowAll(true)}
              className="px-8 py-3 bg-gray-900 text-white rounded-full font-medium hover:bg-gray-800 transition-colors shadow-lg hover:shadow-xl"
            >
              Load More Products
            </button>
          </div>
        )}
      </section>

      {/* FAQ Section */}
      {faqs && faqs.length > 0 && (
        <section className="max-w-4xl mx-auto px-4 py-16 bg-gray-50">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-10">
            Frequently Asked Questions
          </h2>
          <div className="space-y-4">
            {faqs.map((faq, index) => (
              <div
                key={index}
                className="bg-white rounded-lg shadow-md overflow-hidden"
              >
                <button
                  onClick={() => toggleFaq(index)}
                  className="w-full px-6 py-4 flex items-center justify-between text-left hover:bg-gray-50 transition-colors"
                >
                  <span className="font-semibold text-gray-900 pr-4">
                    {faq.question}
                  </span>
                  {openFaqIndex === index ? (
                    <ChevronUp className="w-5 h-5 text-gray-500 flex-shrink-0" />
                  ) : (
                    <ChevronDown className="w-5 h-5 text-gray-500 flex-shrink-0" />
                  )}
                </button>
                {openFaqIndex === index && (
                  <div className="px-6 pb-4 pt-2 text-gray-700 leading-relaxed border-t border-gray-100">
                    {faq.answer}
                  </div>
                )}
              </div>
            ))}
          </div>
        </section>
      )}

{/* Why Choose Our Collection */}
      {categoryData.whyChooseUs && categoryData.whyChooseUs.length > 0 && (
        <section className="bg-gradient-to-br from-gray-50 to-white py-16">
          <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-3xl font-bold text-center text-gray-900 mb-4">
              Why Choose Our {categoryData.displayName} Collection?
            </h2>
            <p className="text-center text-gray-600 mb-10 max-w-2xl mx-auto">
              We carefully curate the best press-on nail designs from trusted Amazon sellers
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {categoryData.whyChooseUs.map((benefit, index) => (
                <div
                  key={index}
                  className="flex items-start gap-4 bg-white rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow"
                >
                  <div className="flex-shrink-0">
                    <div className="w-10 h-10 bg-gradient-to-br from-gray-900 to-gray-700 rounded-full flex items-center justify-center">
                      <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    </div>
                  </div>
                  <p className="text-gray-700 flex-1 pt-2">{benefit}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}
      {/* Related Categories */}
      {categoryData.relatedCategories && categoryData.relatedCategories.length > 0 && (
        <section className="max-w-7xl mx-auto px-4 py-16 bg-gray-50">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-10">
            Explore More Collections
          </h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {categoryData.relatedCategories.map((relatedSlug) => (
              <Link
                key={relatedSlug}
                href={`/shop/${relatedSlug}`}
                className="group bg-white rounded-xl shadow-md hover:shadow-xl transition-all overflow-hidden"
              >
                <div className="aspect-square relative overflow-hidden bg-gray-200 flex items-center justify-center">
                  <span className="text-5xl">💅</span>
                </div>
                <div className="p-4 text-center">
                  <h3 className="font-semibold text-gray-900 group-hover:text-blue-600 transition-colors">
                    {relatedSlug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')} Nails
                  </h3>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Trust Signals */}
      <section className="max-w-7xl mx-auto px-4 py-16 border-t border-gray-200">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
          {/* <div>
            <div className="text-4xl mb-3">🚚</div>
            <h3 className="font-semibold text-gray-900 mb-2">Free Shipping</h3>
            <p className="text-sm text-gray-600">On orders over $25</p>
          </div> */}
          <div>
            <div className="text-4xl mb-3">💯</div>
            <h3 className="font-semibold text-gray-900 mb-2">Quality Guaranteed</h3>
            <p className="text-sm text-gray-600">Premium materials only</p>
          </div>
          <div>
            <div className="text-4xl mb-3">⚡</div>
            <h3 className="font-semibold text-gray-900 mb-2">Easy Application</h3>
            <p className="text-sm text-gray-600">Salon results in 15 minutes</p>
          </div>
          <div>
            <div className="text-4xl mb-3">♻️</div>
            <h3 className="font-semibold text-gray-900 mb-2">Reusable Designs</h3>
            <p className="text-sm text-gray-600">2-3 applications per set</p>
          </div>
        </div>
      </section>

      {/* Affiliate Disclosure */}
      <section className="max-w-7xl mx-auto px-4 py-8 text-center text-sm text-gray-500">
        <p>
          * As an Amazon Associate, we earn from qualifying purchases. Prices shown are
          accurate as of publication and may vary.
        </p>
      </section>

      {/* Float Animation */}
      <style jsx>{`
        @keyframes float {
          0%, 100% {
            transform: translateY(0px) rotate(0deg);
          }
          50% {
            transform: translateY(-20px) rotate(10deg);
          }
        }
        .animate-float {
          animation: float 3s ease-in-out infinite;
        }
      `}</style>
    </div>
  );
}
