// src/app/inspo/page.tsx
import { Metadata } from 'next';
import Link from 'next/link';
import Image from 'next/image';
import { getAllDesignSlugs, getDesignData, getDesignsByCategory } from '@/lib/inspo';

export const metadata: Metadata = {
  title: 'Winter Nail Designs 2025 | 100+ Trending Ideas & Inspiration',
  description: 'Explore 100+ stunning winter nail designs for 2025. From snowflake nails to chrome finishes, burgundy glam & velvet manicures - trending ideas inside!',
  keywords: [
    'winter nail designs 2025',
    'winter nails 2025',
    'winter nail ideas',
    'winter manicure ideas',
    'winter nail art',
    'seasonal nail designs',
    'snowflake nails',
    'chrome winter nails',
    'burgundy winter nails',
    'mocha nails 2025',
    'velvet nail finish',
    'minimalist winter nails',
    'Pantone 2025 nails',
    'festive nail designs',
    'holiday nail inspiration'
  ],
  authors: [{ name: "Mirellé" }],
  creator: "Mirellé",
  publisher: "Mirellé",
  alternates: {
    canonical: 'https://mirelleinspo.com/inspo',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  openGraph: {
    title: 'Winter Nail Designs 2025 | 100+ Trending Ideas & Inspiration',
    description: 'Discover 100+ winter nail designs: snowflake art, chrome finishes, burgundy glam & Pantone 2025 mocha nails. Trending styles for every occasion!',
    url: 'https://mirelleinspo.com/inspo',
    siteName: 'Mirellé',
    locale: 'en_US',
    type: 'website',
    images: [
      {
        url: 'https://mirelleinspo.com/images/inspo/winter-nails-2025-hero.webp',
        width: 1200,
        height: 630,
        alt: 'Gallery of trending winter nail designs 2025 featuring snowflake art, chrome finishes, burgundy wine red and mocha brown manicures',
        type: 'image/webp',
      }
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Winter Nail Designs 2025: 100+ Trending Ideas',
    description: 'Snowflake nails, chrome finishes, burgundy glam & Pantone 2025 mocha. Save these winter nail trends!',
    images: ['https://mirelleinspo.com/images/inspo/winter-nails-2025-hero.webp'],
    creator: "@mirelleinspo",
    site: "@mirelleinspo",
  },
  other: {
    "pin:description": 'Explore 100+ winter nail designs 2025: snowflake art, chrome finishes, burgundy wine red & Pantone mocha nails. Trending styles inside!',
    "pin:media": 'https://mirelleinspo.com/images/inspo/winter-nails-2025-hero.webp',
    "pinterest-rich-pin": "true",
    "og:image:width": "1200",
    "og:image:height": "630",
    "og:image:alt": 'Gallery of trending winter nail designs 2025 featuring snowflake art, chrome finishes, burgundy wine red and mocha brown manicures',
    "og:image:type": "image/webp",
    "article:publisher": "https://www.pinterest.com/mirelle_inspo",
    "pinterest:category": "winter nail designs 2025",
    "pinterest:board_suggestion": "Winter Nail Art Ideas",
    "og:see_also": "https://mirelleinspo.com/inspo",
  },
};

export default async function InspoPage() {
  const designSlugs = getAllDesignSlugs();
  const designs = designSlugs.map(slug => getDesignData(slug)).filter(Boolean);
  const designsByCategory = getDesignsByCategory();

  // Category display order for Winter 2025
  const categoryOrder = ['Seasonal', 'Trendy', 'Classic'];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-cyan-50">
      {/* Hero Section with Winter Theme */}
      <section className="relative overflow-hidden">
        {/* Animated gradient background */}
        <div className="absolute inset-0 bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900 opacity-95" />
        
        {/* Animated snowflakes */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute top-10 left-[10%] text-white/20 text-6xl animate-float-slow">❄️</div>
          <div className="absolute top-20 right-[15%] text-white/30 text-4xl animate-float-slower">❄</div>
          <div className="absolute top-40 left-[25%] text-white/10 text-8xl animate-float-slowest">❄️</div>
          <div className="absolute bottom-20 right-[20%] text-white/20 text-5xl animate-float-slow">✨</div>
          <div className="absolute bottom-40 left-[30%] text-white/15 text-7xl animate-float-slower">❄</div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32 text-center">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/20 px-5 py-2 rounded-full text-white text-sm font-medium mb-6 shadow-lg animate-fade-in">
            <span className="w-2 h-2 bg-cyan-400 rounded-full animate-pulse" />
            Updated Weekly • 285+ Designs • Winter 2025
          </div>
          
          <h1 className="font-display text-5xl md:text-6xl lg:text-7xl font-bold mb-6 tracking-tight text-white animate-slide-up">
            Winter Nail Designs 2025
          </h1>
          
          <p className="text-xl md:text-2xl text-white/90 mb-8 max-w-3xl mx-auto font-light leading-relaxed animate-slide-up animation-delay-100">
            Discover 285+ stunning winter nail designs from delicate snowflakes to chrome finishes, 
            burgundy elegance & Pantone's Mocha Mousse. Find your perfect winter manicure.
          </p>

          {/* Feature Pills */}
          <div className="flex flex-wrap gap-3 justify-center text-sm mb-10 animate-slide-up animation-delay-200">
            <span className="bg-white/20 backdrop-blur-sm border border-white/30 px-4 py-2 rounded-full text-white font-medium">
              ❄️ Snowflake Art
            </span>
            <span className="bg-white/20 backdrop-blur-sm border border-white/30 px-4 py-2 rounded-full text-white font-medium">
              ✨ Chrome Finishes
            </span>
            <span className="bg-white/20 backdrop-blur-sm border border-white/30 px-4 py-2 rounded-full text-white font-medium">
              🍷 Burgundy Glam
            </span>
            <span className="bg-white/20 backdrop-blur-sm border border-white/30 px-4 py-2 rounded-full text-white font-medium">
              🍫 Pantone 2025
            </span>
            <span className="bg-white/20 backdrop-blur-sm border border-white/30 px-4 py-2 rounded-full text-white font-medium">
              💎 Velvet Textures
            </span>
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-wrap gap-4 justify-center animate-slide-up animation-delay-300">
            <Link 
              href="#categories"
              className="group bg-white text-burgundy-700 px-8 py-4 rounded-full font-semibold text-lg shadow-xl hover:shadow-2xl hover:scale-105 transition-all duration-300 inline-flex items-center gap-2"
            >
              Browse Gallery
              <svg className="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </Link>
            <Link 
              href="#trending"
              className="bg-white/10 backdrop-blur-md border-2 border-white/40 text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-white/20 transition-all duration-300"
            >
              What's Trending
            </Link>
          </div>
        </div>

        {/* Wave Divider */}
        <div className="absolute bottom-0 left-0 right-0">
          <svg className="w-full h-12 md:h-20 fill-white" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" />
          </svg>
        </div>
      </section>

      {/* Winter Trends Section */}
      <section id="trending" className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl md:text-5xl font-display font-bold text-gray-900 mb-4">
              Top Winter 2025 Trends
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              What's hot this winter? From runway-inspired designs to viral TikTok trends
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Trend Card 1 */}
            <div className="group bg-gradient-to-br from-amber-50 to-orange-50 rounded-3xl p-8 border border-orange-100 hover:shadow-2xl transition-all duration-300">
              <div className="text-5xl mb-4">🍫</div>
              <h3 className="text-2xl font-bold text-gray-900 mb-3">Mocha Mousse</h3>
              <p className="text-gray-700 mb-4 leading-relaxed">
                Pantone Color of the Year 2025 dominates runways. Chocolate, espresso & caramel tones trending on Instagram.
              </p>
              <Link href="/inspo/chocolate-brown-winter-nails" className="text-burgundy-700 font-semibold inline-flex items-center gap-2 group-hover:gap-3 transition-all">
                Explore Brown Nails
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>

            {/* Trend Card 2 */}
            <div className="group bg-gradient-to-br from-slate-50 to-zinc-50 rounded-3xl p-8 border border-slate-200 hover:shadow-2xl transition-all duration-300">
              <div className="text-5xl mb-4">✨</div>
              <h3 className="text-2xl font-bold text-gray-900 mb-3">Aurora Chrome</h3>
              <p className="text-gray-700 mb-4 leading-relaxed">
                Icy metallic finishes with holographic shimmer. Silver, platinum & pearl vanilla creating mirror effects.
              </p>
              <Link href="/inspo/chrome-metallic-winter-nails" className="text-burgundy-700 font-semibold inline-flex items-center gap-2 group-hover:gap-3 transition-all">
                See Chrome Designs
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>

            {/* Trend Card 3 */}
            <div className="group bg-gradient-to-br from-emerald-50 to-teal-50 rounded-3xl p-8 border border-emerald-100 hover:shadow-2xl transition-all duration-300">
              <div className="text-5xl mb-4">🐱</div>
              <h3 className="text-2xl font-bold text-gray-900 mb-3">Velvet Textures</h3>
              <p className="text-gray-700 mb-4 leading-relaxed">
                Dimensional magnetic polish with cat-eye effects. Emerald, navy & ruby creating luxury plush aesthetic.
              </p>
              <Link href="/inspo/velvet-cat-eye-winter-nails" className="text-burgundy-700 font-semibold inline-flex items-center gap-2 group-hover:gap-3 transition-all">
                Discover Velvet Nails
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Categories Grid */}
      <section id="categories" className="py-20 bg-gradient-to-br from-slate-50 via-white to-blue-50">
        {categoryOrder.map(categoryName => {
          const categoryDesigns = designsByCategory[categoryName];
          if (!categoryDesigns || categoryDesigns.length === 0) return null;

          const categoryInfo = {
            'Seasonal': {
              title: 'Seasonal Winter Designs',
              description: 'Perfect designs for the coldest season of the year',
              emoji: '❄️'
            },
            'Trendy': {
              title: 'Trending Styles',
              description: 'Latest viral nail trends and modern winter finishes',
              emoji: '🔥'
            },
            'Classic': {
              title: 'Timeless Elegance',
              description: 'Sophisticated designs that never go out of style',
              emoji: '💎'
            }
          }[categoryName];

          return (
            <div key={categoryName} className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20 last:mb-0">
              <div className="mb-12 text-center">
                <div className="inline-block text-5xl mb-4">{categoryInfo.emoji}</div>
                <h2 className="text-4xl md:text-5xl font-display font-bold text-gray-900 mb-3">
                  {categoryInfo.title}
                </h2>
                <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                  {categoryInfo.description}
                </p>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {categoryDesigns.map((design) => {
                  if (!design) return null;
                  
                  return (
                    <Link
                      key={design.slug}
                      href={`/inspo/${design.slug}`}
                      className="group relative bg-white rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 overflow-hidden"
                    >
                      {/* Design Image with Fallback */}
                      <div className="relative h-96 overflow-hidden bg-gradient-to-br from-gray-100 to-gray-200">
                        {design.heroImage.startsWith('/') ? (
                          <Image
                            src={design.heroImage}
                            alt={`${design.displayName} nail design inspiration for winter 2025`}
                            fill
                            className="object-cover transform group-hover:scale-110 transition-transform duration-700"
                            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                          />
                        ) : (
                          <div
                            className="absolute inset-0 bg-cover bg-center transform group-hover:scale-110 transition-transform duration-700"
                            style={{ backgroundImage: `url(${design.heroImage})` }}
                          />
                        )}
                        
                        {/* Gradient overlay */}
                        <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent group-hover:from-black/70 transition-all duration-500" />
                        
                        {/* Category badge */}
                        <div className="absolute top-4 right-4 bg-white/20 backdrop-blur-md border border-white/40 px-4 py-2 text-white text-xs font-bold uppercase tracking-wider rounded-full">
                          {design.category}
                        </div>

                        {/* Emoji */}
                        <div className="absolute top-4 left-4 text-3xl drop-shadow-lg">
                          {design.emojis[0]}
                        </div>
                        
                        {/* Design Info Overlay */}
                        <div className="absolute bottom-0 left-0 right-0 p-6 text-white">
                          <h3 className="text-2xl md:text-3xl font-display font-bold mb-2 group-hover:text-cyan-300 transition-colors">
                            {design.displayName}
                          </h3>
                          <p className="text-white/90 mb-4 text-sm md:text-base leading-relaxed">
                            {design.description}
                          </p>
                          
                          {/* Key takeaways pills */}
                          {design.tldr?.keyTakeaways && (
                            <div className="flex flex-wrap gap-2 mb-4">
                              {design.tldr.keyTakeaways.slice(0, 2).map((takeaway, idx) => (
                                <span key={idx} className="px-3 py-1 bg-white/20 backdrop-blur-sm rounded-full text-xs font-medium border border-white/30">
                                  {takeaway}
                                </span>
                              ))}
                            </div>
                          )}
                          
                          <div className="inline-flex items-center text-white font-semibold border-b-2 border-transparent group-hover:border-cyan-300 transition-all">
                            View Gallery
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
            </div>
          );
        })}
      </section>

      {/* Why Choose Section */}
      <section className="bg-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl md:text-5xl font-display font-bold text-gray-900 mb-12 text-center">
            Why Mirellé for Winter Nail Inspiration?
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div className="text-center group">
              <div className="w-20 h-20 bg-gradient-to-br from-blue-100 to-cyan-100 rounded-3xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg">
                <svg className="w-10 h-10 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 mb-3">285+ Winter Designs</h3>
              <p className="text-gray-600 leading-relaxed">
                Curated collection updated weekly with latest winter trends and timeless classics
              </p>
            </div>

            <div className="text-center group">
              <div className="w-20 h-20 bg-gradient-to-br from-purple-100 to-pink-100 rounded-3xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg">
                <svg className="w-10 h-10 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 mb-3">Trend Insights</h3>
              <p className="text-gray-600 leading-relaxed">
                Stay ahead with runway-inspired designs and TikTok viral trends explained
              </p>
            </div>

            <div className="text-center group">
              <div className="w-20 h-20 bg-gradient-to-br from-rose-100 to-red-100 rounded-3xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg">
                <svg className="w-10 h-10 text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                </svg>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 mb-3">All Occasions</h3>
              <p className="text-gray-600 leading-relaxed">
                From winter weddings to holiday parties - find perfect nails for every event
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

// Add custom animation delays
const styles = `
  @keyframes float-slow {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(10deg); }
  }
  @keyframes float-slower {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-30px) rotate(-10deg); }
  }
  @keyframes float-slowest {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-40px) rotate(15deg); }
  }
  .animate-float-slow {
    animation: float-slow 8s ease-in-out infinite;
  }
  .animate-float-slower {
    animation: float-slower 12s ease-in-out infinite;
  }
  .animate-float-slowest {
    animation: float-slowest 15s ease-in-out infinite;
  }
  .animation-delay-100 {
    animation-delay: 0.1s;
  }
  .animation-delay-200 {
    animation-delay: 0.2s;
  }
  .animation-delay-300 {
    animation-delay: 0.3s;
  }
`;
