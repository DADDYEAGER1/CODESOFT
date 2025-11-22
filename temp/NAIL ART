
import Image from 'next/image';
import Link from 'next/link';
import { Metadata } from 'next';

// SEO Metadata Export
export const metadata: Metadata = {
  title: 'Easy Nail Designs for Beginners: 20+ Simple Ideas (2025) | Mirellé',
  description: 'Master easy nail designs for beginners with no tools needed! 20+ simple tutorials using toothpicks, tape & household items. Perfect for first-timers. Start creating!',
  keywords: [
    'easy nail designs for beginners',
    'simple nail art step by step',
    'beginner nail art tutorial',
    'easy nail art ideas at home',
    'simple nail art without tools',
    'nail designs for beginners at home',
    'easy DIY nail designs',
    'beginner friendly nail art',
    'simple nail designs',
    'easy manicure ideas',
    'nail art for first timers',
    'quick easy nail designs'
  ],
  authors: [{ name: 'Mirellé Team', url: 'https://mirelleinspo.com/about' }],
  creator: 'Mirellé',
  publisher: 'Mirellé',
  alternates: {
    canonical: 'https://mirelleinspo.com/topics/nail-art-guides',
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
    title: 'Easy Nail Designs for Beginners: 20+ Simple Ideas (2025)',
    description: 'Complete beginner? Try these 20+ easy nail designs at home with zero experience. Simple step-by-step tutorials, no fancy tools required!',
    type: 'article',
    url: 'https://mirelleinspo.com/topics/nail-art-guides',
    siteName: 'Mirellé',
    locale: 'en_US',
    images: [{
      url: 'https://mirelleinspo.com/nail-art-hero-beginner-designs-progression.jpg',
      width: 1200,
      height: 630,
      alt: 'Easy nail art designs for beginners showing simple to advanced progression with household tools',
    }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Easy Nail Designs for Beginners: 20+ Simple Ideas (2025)',
    description: 'Zero experience? No problem! 20+ easy nail tutorials with household items only',
    images: ['https://mirelleinspo.com/nail-art-hero-beginner-designs-progression.jpg'],
    creator: '@mirelleinspo',
  },
};

export default function NailArtGuides() {
  // JSON-LD Structured Data
  const baseUrl = 'https://mirelleinspo.com';
  
  // 1. Article Schema
  const articleSchema = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    '@id': `${baseUrl}/topics/nail-art-guides#article`,
    headline: 'Easy Nail Designs for Beginners: 20+ Simple Step-by-Step Tutorials',
    description: 'Complete beginner guide to nail art with 20+ easy designs using household items. No special tools needed, perfect for first-timers starting their nail art journey.',
    image: {
      '@type': 'ImageObject',
      url: `${baseUrl}/nail-art-hero-beginner-designs-progression.jpg`,
      width: 1200,
      height: 630,
      caption: 'Beginner nail art progression from simple dots to detailed designs'
    },
    author: {
      '@type': 'Person',
      '@id': `${baseUrl}/#mirelle-team`,
      name: 'Mirellé Team',
      url: `${baseUrl}/about`
    },
    publisher: {
      '@type': 'Organization',
      '@id': `${baseUrl}/#organization`,
      name: 'Mirellé',
      logo: {
        '@type': 'ImageObject',
        url: `${baseUrl}/apple-touch-icon.png`
      }
    },
    datePublished: '2025-01-15',
    dateModified: '2025-01-15',
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': `${baseUrl}/topics/nail-art-guides`
    },
    articleSection: 'Nail Art Tutorials',
    keywords: 'easy nail designs for beginners, simple nail art, beginner nail tutorial, DIY nail art at home',
    inLanguage: 'en-US'
  };

  // 2. BreadcrumbList Schema
  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'Home',
        item: baseUrl
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: 'Topics',
        item: `${baseUrl}/topics`
      },
      {
        '@type': 'ListItem',
        position: 3,
        name: 'Nail Art Guides',
        item: `${baseUrl}/topics/nail-art-guides`
      }
    ]
  };

  // 3. FAQ Schema
  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: [
      {
        '@type': 'Question',
        name: 'How do I start doing nail art as a beginner?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Start with the simplest designs like single color perfection or random dots using household items you already have. Practice basic application first, then progress to easy designs using toothpicks for dots, tape for stripes, and sponges for gradients. Focus on mastering one technique before moving to the next.'
        }
      },
      {
        '@type': 'Question',
        name: 'What is the easiest nail design for first timers?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Random dots are the easiest nail design for first-timers because there is no pattern to follow and mistakes look intentional. Use a toothpick dipped in polish to create scattered dots across a base color. This forgiving design builds confidence while teaching basic tool control and color coordination.'
        }
      },
      {
        '@type': 'Question',
        name: 'Can I do nail art without any tools?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Yes, you can create beautiful nail art with household items. Use toothpicks for dots and lines, bobby pins for double dots and hearts, scotch tape for stripes, makeup sponges for ombre, and cotton swabs with acetone for cleanup. No special nail art tools are required to start.'
        }
      },
      {
        '@type': 'Question',
        name: 'What nail designs are best for beginners?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Best beginner designs include polka dots, simple French tips, vertical stripes with tape, glitter gradients, one-finger accent nails, and basic color blocking. These designs require minimal precision, use simple techniques, and look impressive despite being easy to execute with basic household items.'
        }
      },
      {
        '@type': 'Question',
        name: 'How do I make dots on my nails at home?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Dip a toothpick into nail polish and gently press onto your nail surface. For smaller dots, use the pointed end. For larger dots, use the blunt end or a bobby pin head. Let the base color dry completely first. Practice the pressure needed on paper before trying on nails.'
        }
      },
      {
        '@type': 'Question',
        name: 'What can I use instead of a dotting tool?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Toothpicks, bobby pins, pencil erasers, ballpoint pen tips, or even the head of a sewing pin make excellent dotting tool substitutes. Bobby pins create perfect double dots for easy designs. Toothpick tips offer varying dot sizes depending on which end you use.'
        }
      },
      {
        '@type': 'Question',
        name: 'How do I do simple French tips at home?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Apply a sheer pink or nude base coat first. Let dry completely. Use scotch tape or striping tape to mark the smile line across your nail tip. Paint white polish over the tip area, let dry 30 seconds, then carefully remove tape. Seal with clear top coat for smooth finish.'
        }
      },
      {
        '@type': 'Question',
        name: 'What is an easy nail art design for short nails?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Half moon manicure, tiny dots, micro French tips, single accent nail, and vertical stripes all work beautifully on short nails. These designs do not require length to look elegant. Focus on horizontal or minimal patterns that enhance the nail shape rather than require extended canvas space.'
        }
      },
      {
        '@type': 'Question',
        name: 'How long does nail art take for beginners?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Simple designs take 5 to 10 minutes per hand for beginners including drying time between steps. Your first attempts may take 15 to 20 minutes as you learn techniques. With practice, most easy designs become faster. Allow 30 minutes total for full manicure including prep, base coat, design, and top coat.'
        }
      },
      {
        '@type': 'Question',
        name: 'Can I do nail art with just nail polish?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Yes, you need only nail polish plus household items. Base coat, two or more polish colors, and top coat are essential. Add toothpicks, tape, and sponges you already own. No special brushes, gels, or equipment required. Regular polish works perfectly for all beginner designs in this guide.'
        }
      },
      {
        '@type': 'Question',
        name: 'What colors are easiest for nail art beginners?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Start with high-contrast color combinations like black on white, white on navy, or gold on burgundy. These contrasts make designs visible and mistakes less obvious. Avoid sheer or similar-toned colors initially. Nude base with bright accent colors offers forgiving canvas for learning technique.'
        }
      },
      {
        '@type': 'Question',
        name: 'How do I keep my hand steady for nail art?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Rest both elbows on a table or firm surface. Work in good lighting. Take breaks if hands get tired or shaky. Practice designs on paper first to build muscle memory. Consider working in short sessions rather than rushing. Caffeine can increase shakiness so avoid before nail art sessions.'
        }
      },
      {
        '@type': 'Question',
        name: 'What is the simplest nail design to try first?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Single color perfection is the simplest starting point to master basic polish application. Once comfortable, try random dots with a toothpick which requires no pattern or precision. These foundational skills build confidence before progressing to designs requiring more control like stripes or French tips.'
        }
      },
      {
        '@type': 'Question',
        name: 'Do I need special brushes for nail art?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'No special brushes are needed for beginner nail art. Use the brush inside your polish bottle for base application. Toothpicks, tape, and sponges create all the designs in this guide. Once you advance, a thin striping brush and cleanup brush are helpful but not essential initially.'
        }
      },
      {
        '@type': 'Question',
        name: 'Can I use a toothpick for nail designs?',
        acceptedAnswer: {
          '@type': 'Answer',
          text: 'Toothpicks are perfect for nail art. Use the pointed end for tiny dots and fine lines. Use the blunt end for larger dots. Drag through wet polish to create marble effects, swirls, or floral designs. Toothpicks offer excellent control and precision for beginners at zero cost.'
        }
      }
    ]
  };

  // 4. HowTo Schema
  const howToSchema = {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: 'How to Do Easy Nail Art for Beginners Using Household Items',
    description: 'Complete beginner tutorial for creating simple nail art designs using only household items like toothpicks, tape, and makeup sponges',
    image: {
      '@type': 'ImageObject',
      url: `${baseUrl}/nail-art-household-tools-setup-beginner.jpg`
    },
    totalTime: 'PT30M',
    estimatedCost: {
      '@type': 'MonetaryAmount',
      currency: 'USD',
      value: '15'
    },
    supply: [
      { '@type': 'HowToSupply', name: 'Base coat' },
      { '@type': 'HowToSupply', name: 'Nail polish in 2-3 colors' },
      { '@type': 'HowToSupply', name: 'Top coat' },
      { '@type': 'HowToSupply', name: 'Toothpicks' },
      { '@type': 'HowToSupply', name: 'Bobby pins' },
      { '@type': 'HowToSupply', name: 'Scotch tape or striping tape' },
      { '@type': 'HowToSupply', name: 'Makeup sponge' },
      { '@type': 'HowToSupply', name: 'Cotton swabs' },
      { '@type': 'HowToSupply', name: 'Acetone or nail polish remover' }
    ],
    tool: [
      { '@type': 'HowToTool', name: 'Table or flat surface' },
      { '@type': 'HowToTool', name: 'Good lighting' }
    ],
    step: [
      {
        '@type': 'HowToStep',
        position: 1,
        name: 'Prep Your Nails',
        text: 'Clean nails with soap and water. Push back cuticles gently. File nails into desired shape. Buff nail surface lightly to remove ridges. This creates smooth canvas for polish.',
        image: `${baseUrl}/nail-art-prep-clean-file-buff-cuticles.jpg`
      },
      {
        '@type': 'HowToStep',
        position: 2,
        name: 'Apply Base Coat',
        text: 'Paint thin layer of base coat on all nails. Start at base, swipe to tip in three strokes. Let dry 2 minutes. Base coat protects nails and helps polish adhere.',
        image: `${baseUrl}/nail-art-base-coat-application-technique.jpg`
      },
      {
        '@type': 'HowToStep',
        position: 3,
        name: 'Apply Base Color',
        text: 'Paint two thin coats of your chosen base color. Wait 2 minutes between coats. Thin coats prevent bubbles and dry faster than one thick coat.',
        image: `${baseUrl}/nail-art-base-color-two-thin-coats.jpg`
      },
      {
        '@type': 'HowToStep',
        position: 4,
        name: 'Create Your Design',
        text: 'Once base color is completely dry, add your chosen design using household tools. Toothpicks for dots, tape for lines, sponge for gradients. Work on one nail at a time.',
        image: `${baseUrl}/nail-art-design-application-toothpick-dots.jpg`
      },
      {
        '@type': 'HowToStep',
        position: 5,
        name: 'Clean Up Edges',
        text: 'Dip cotton swab in acetone. Carefully clean polish from skin and cuticles. This makes design look professional and polished.',
        image: `${baseUrl}/nail-art-cleanup-acetone-cotton-swab.jpg`
      },
      {
        '@type': 'HowToStep',
        position: 6,
        name: 'Seal with Top Coat',
        text: 'Apply thin layer of top coat over entire nail including tip. This seals design, adds shine, and prevents chipping. Let dry 5 minutes before touching anything.',
        image: `${baseUrl}/nail-art-top-coat-sealing-glossy-finish.jpg`
      }
    ]
  };

  // 5. WebPage Schema
  const webPageSchema = {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    '@id': `${baseUrl}/topics/nail-art-guides`,
    url: `${baseUrl}/topics/nail-art-guides`,
    name: 'Easy Nail Art Guides for Beginners: 20+ Simple Designs You Can Do at Home',
    description: 'Complete beginner-friendly nail art tutorials using only household items. Learn 20+ easy designs from dots to ombre with step-by-step instructions.',
    inLanguage: 'en-US',
    isPartOf: {
      '@type': 'WebSite',
      '@id': `${baseUrl}/#website`
    },
    about: {
      '@type': 'Thing',
      name: 'Nail Art for Beginners'
    },
    primaryImageOfPage: {
      '@type': 'ImageObject',
      url: `${baseUrl}/nail-art-hero-beginner-designs-progression.jpg`
    }
  };

  // 6. ItemList Schema
  const itemListSchema = {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: '20+ Easy Nail Designs for Beginners',
    description: 'Comprehensive list of beginner-friendly nail art designs organized by difficulty level with household tools only',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Single Color Perfection' },
      { '@type': 'ListItem', position: 2, name: 'Simple Glitter Tips' },
      { '@type': 'ListItem', position: 3, name: 'One-Finger Accent Nail' },
      { '@type': 'ListItem', position: 4, name: 'Half and Half Color Block' },
      { '@type': 'ListItem', position: 5, name: 'Random Dots' },
      { '@type': 'ListItem', position: 6, name: 'Classic Polka Dots' },
      { '@type': 'ListItem', position: 7, name: 'Simple French Tips' },
      { '@type': 'ListItem', position: 8, name: 'Vertical Stripes' },
      { '@type': 'ListItem', position: 9, name: 'Glitter Gradient' },
      { '@type': 'ListItem', position: 10, name: 'Ombre Two-Tone' },
      { '@type': 'ListItem', position: 11, name: 'Tiny Hearts' },
      { '@type': 'ListItem', position: 12, name: 'Simple Floral 5-Dot Flower' },
      { '@type': 'ListItem', position: 13, name: 'Negative Space Lines' },
      { '@type': 'ListItem', position: 14, name: 'Confetti Nails' },
      { '@type': 'ListItem', position: 15, name: 'Marble Effect' },
      { '@type': 'ListItem', position: 16, name: 'Micro French Tips' },
      { '@type': 'ListItem', position: 17, name: 'Aura Nails' },
      { '@type': 'ListItem', position: 18, name: 'Abstract Minimalist' },
      { '@type': 'ListItem', position: 19, name: 'Glass Nails' },
      { '@type': 'ListItem', position: 20, name: 'Mocha Mousse Solid' },
      { '@type': 'ListItem', position: 21, name: 'Soap Nails' },
      { '@type': 'ListItem', position: 22, name: 'Jelly Nails' }
    ]
  };

  // 7. ImageGallery Schema
  const imageGallerySchema = {
    '@context': 'https://schema.org',
    '@type': 'ImageGallery',
    name: 'Beginner Nail Art Designs Photo Tutorial Gallery',
    description: 'Visual step-by-step guide showing easy nail art techniques for complete beginners using household items',
    image: [
      {
        '@type': 'ImageObject',
        contentUrl: `${baseUrl}/nail-art-household-tools-toothpick-bobby-pin-tape-sponge.jpg`,
        caption: 'Household items that work as nail art tools including toothpicks, bobby pins, tape, and makeup sponges'
      },
      {
        '@type': 'ImageObject',
        contentUrl: `${baseUrl}/nail-art-polka-dots-toothpick-technique-tutorial.jpg`,
        caption: 'Step by step polka dot nail art technique using toothpick showing pressure and dot placement'
      },
      {
        '@type': 'ImageObject',
        contentUrl: `${baseUrl}/nail-art-simple-french-tips-tape-method-beginner.jpg`,
        caption: 'Simple French tips tutorial using scotch tape guide for clean smile line'
      }
    ]
  };

  return (
    <>
      {/* Structured Data Scripts */}
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(howToSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(webPageSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(itemListSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(imageGallerySchema) }} />

      <div className="min-h-screen">
        {/* Hero Section */}
        <section className="relative h-[70vh] min-h-[500px] flex items-center justify-center overflow-hidden">
          <div className="absolute inset-0 z-0">
            <img
              src="/nail-art-hero-beginner-designs-progression.jpg"
              alt="Easy nail art designs for beginners showing simple to advanced progression with household tools"
              className="w-full h-full object-cover"
            />
            <div className="absolute inset-0 bg-gradient-to-b from-black/40 to-black/70" />
          </div>
          
          <div className="relative z-10 text-center text-white max-w-4xl px-6">
            <div className="inline-flex items-center glass-card-dark px-4 py-2 rounded-full text-sm mb-4 backdrop-blur-sm">
              ✨ Beginner-Friendly Guide • 20-minute read • Updated January 2025
            </div>
            
            <h1 className="font-serif text-5xl md:text-7xl font-bold mb-6 animate-fade-in">
              Easy Nail Designs for Beginners
            </h1>
            
            <p className="text-xl md:text-2xl font-light mb-8 text-gray-100">
              20+ simple tutorials using stuff you already have at home—no fancy tools required
            </p>
            
            <div className="flex justify-center gap-4 flex-wrap">
              <a href="#quick-nav" className="bg-burgundy-600 hover:bg-burgundy-700 px-8 py-4 rounded-full font-semibold transition-all transform hover:scale-105 shadow-xl">
                Start Learning
              </a>
              <a href="#faq" className="glass-card px-8 py-4 rounded-full font-semibold hover:bg-white/20 transition-all">
                Jump to FAQs
              </a>
            </div>
          </div>
          
          <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
            <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
            </svg>
          </div>
        </section>

        {/* Quick Navigation TLDR Section */}
        <section id="quick-nav" className="py-16 bg-gradient-to-r from-burgundy-50 via-pink-50 to-purple-50">
          <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="glass-card p-8 rounded-2xl">
              <h2 className="font-serif text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center">
                🎯 Your Nail Art Roadmap
              </h2>
              <p className="text-center text-gray-600 mb-8">
                This is a long guide. Here's exactly where everything is so you can jump straight to what you need.
              </p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Quick Links Column 1 */}
                <div className="space-y-4">
                  <a href="#why-not-hard" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">🤔 Why Nail Art Isn't Hard</div>
                    <div className="text-sm text-gray-600">Debunking myths about skill, cost, and time</div>
                  </a>
                  
                  <a href="#supplies" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">🛠️ What You Actually Need</div>
                    <div className="text-sm text-gray-600">Household items you already own (under $15 total)</div>
                  </a>
                  
                  <a href="#nail-prep" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">💅 Nail Prep 101</div>
                    <div className="text-sm text-gray-600">The 5-minute prep that makes everything easier</div>
                  </a>
                  
                  <a href="#ultra-easy" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">⭐ Ultra Easy Designs (START HERE!)</div>
                    <div className="text-sm text-gray-600">5 designs that literally anyone can do</div>
                  </a>
                  
                  <a href="#super-easy" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">✨ Super Easy Designs</div>
                    <div className="text-sm text-gray-600">7 slightly fancier looks (still beginner-friendly)</div>
                  </a>
                  
                  <a href="#still-easy" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">💫 Still Easy Designs</div>
                    <div className="text-sm text-gray-600">6 designs once you've got the basics down</div>
                  </a>
                </div>

                {/* Quick Links Column 2 */}
                <div className="space-y-4">
                  <a href="#trending-2025" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">🔥 Trending 2025 Beginner Designs</div>
                    <div className="text-sm text-gray-600">What's popular AND actually doable right now</div>
                  </a>
                  
                  <a href="#mistakes" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">❌ Mistakes to Avoid</div>
                    <div className="text-sm text-gray-600">The 7 things that trip up every beginner</div>
                  </a>
                  
                  <a href="#non-dominant" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">🤚 Non-Dominant Hand Strategies</div>
                    <div className="text-sm text-gray-600">How to make your left hand not look terrible</div>
                  </a>
                  
                  <a href="#trends" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">🌟 2025 Nail Trends</div>
                    <div className="text-sm text-gray-600">Why this year is perfect for beginners</div>
                  </a>
                  
                  <a href="#nail-health" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">🏥 Nail Health & Safety</div>
                    <div className="text-sm text-gray-600">Keeping your nails healthy while having fun</div>
                  </a>
                  
                  <a href="#faq" style={{color: '#2563eb', textDecoration: 'underline'}} className="block p-4 bg-white rounded-lg hover:shadow-md transition-shadow">
                    <div className="font-semibold mb-1">❓ FAQs</div>
                    <div className="text-sm text-gray-600">15 most-asked beginner questions answered</div>
                  </a>
                </div>
              </div>

              <div className="mt-8 p-6 bg-burgundy-50 rounded-xl border-l-4 border-burgundy-600">
                <h3 className="font-bold text-gray-900 mb-2">📍 First time here?</h3>
                <p className="text-gray-700 text-sm">
                  Start with <a href="#ultra-easy" style={{color: '#2563eb', textDecoration: 'underline'}}>Ultra Easy Designs</a> (seriously, anyone can do these). Once you nail those (pun intended), move to <a href="#super-easy" style={{color: '#2563eb', textDecoration: 'underline'}}>Super Easy</a>. Don't skip ahead or you'll get frustrated. Trust the process!
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Quick Stats Bar */}
        <section className="py-12 bg-white">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="glass-card p-6 rounded-2xl text-center">
                <div className="w-16 h-16 bg-burgundy-600 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-3xl">🎨</span>
                </div>
                <div className="text-3xl font-bold text-burgundy-600 mb-2">20+</div>
                <p className="text-gray-600 text-sm">Beginner-friendly designs you can actually do at home</p>
                <p className="text-xs text-gray-400 mt-2">No salon experience needed</p>
              </div>
              <div className="glass-card p-6 rounded-2xl text-center">
                <div className="w-16 h-16 bg-pink-600 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-3xl">💰</span>
                </div>
                <div className="text-3xl font-bold text-pink-600 mb-2">Under $15</div>
                <p className="text-gray-600 text-sm">Total cost to start with household items you already own</p>
                <p className="text-xs text-gray-400 mt-2">Budget-friendly nail art</p>
              </div>
              <div className="glass-card p-6 rounded-2xl text-center">
                <div className="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-3xl">⏱️</span>
                </div>
                <div className="text-3xl font-bold text-purple-600 mb-2">5-15 min</div>
                <p className="text-gray-600 text-sm">Average time per design for beginners including drying time</p>
                <p className="text-xs text-gray-400 mt-2">Quick & achievable results</p>
              </div>
            </div>
          </div>
        </section>

        {/* Main Content */}
        <section id="content" className="py-20 bg-white">
          <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            
            {/* Introduction */}
            <div className="mb-16">
              <p className="text-lg text-gray-600 leading-relaxed mb-6">
                Think nail art is only for people with steady hands and hours of free time? I get it—scrolling through Instagram makes it look impossible.
              </p>
              <p className="text-lg text-gray-600 leading-relaxed mb-6">
                Here's the thing though: those perfect posts are usually done by professionals with years of practice. What you don't see are the three attempts before that photo, the special equipment, or the hour it actually took.
              </p>
              <p className="text-lg text-gray-600 leading-relaxed">
                This guide is different. Every design here is something you can do on your first try using stuff you already have at home. No dotting tools, no special brushes, no artistic talent required. Just toothpicks, tape, and regular nail polish. Let's break down exactly how to create <a href="https://mirelleinspo.com/topics/seasonal-trends" style={{color: '#2563eb', textDecoration: 'underline'}}>trending nail looks</a> without the intimidation factor.
              </p>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 1: Why Nail Art Isn't Hard */}
            <div id="why-not-hard" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                🤔 Why Nail Art Isn't as Hard as You Think
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-6">
                Let's bust some myths real quick because these false beliefs stop so many people from even trying.
              </p>

              <div className="space-y-6 mb-8">
                <div className="glass-card p-6 rounded-xl border-l-4 border-burgundy-400">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">❌</span>
                    Myth: "You need artistic talent"
                  </h3>
                  <p className="text-gray-600 text-sm mb-2">
                    <strong>Reality:</strong> Most beginner nail art is just dots, lines, and tape. If you can press a toothpick onto your nail, you can do polka dots. If you can place tape in a straight line, you can do stripes. Zero drawing skills needed.
                  </p>
                  <p className="text-gray-600 text-sm">
                    The designs in this guide require precision, not artistry. Think of it like coloring inside the lines, not creating the Mona Lisa.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl border-l-4 border-pink-400">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">❌</span>
                    Myth: "You need expensive tools"
                  </h3>
                  <p className="text-gray-600 text-sm mb-2">
                    <strong>Reality:</strong> Your kitchen drawer has better nail art tools than some salons. Toothpicks work better than dotting tools for beginners because you can control the pressure easier. Bobby pins create perfect double dots. Scotch tape makes cleaner lines than striping brushes when you're starting out.
                  </p>
                  <p className="text-gray-600 text-sm">
                    Total investment to try every design in this guide: about $15 for base coat, a few polish colors, and top coat. You already own the rest.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl border-l-4 border-purple-400">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">❌</span>
                    Myth: "It takes forever"
                  </h3>
                  <p className="text-gray-600 text-sm">
                    <strong>Reality:</strong> The simplest designs take 5-10 minutes total. Even the more detailed ones max out at 15-20 minutes for both hands. That's less time than scrolling TikTok while your regular manicure dries.
                  </p>
                </div>
              </div>

              <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-2xl p-8 border-l-4 border-green-600">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-green-600 rounded-xl flex items-center justify-center flex-shrink-0">
                    <span className="text-2xl">💡</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-gray-900 mb-2 text-lg">Real Talk</h4>
                    <p className="text-gray-700">
                      The actual reason nail art feels hard is because most tutorials skip the beginner steps. They assume you already know how to apply polish evenly, work with your non-dominant hand, and control a toothpick. This guide assumes you know nothing and walks you through everything.
                    </p>
                  </div>
                </div>
              </div>

              <h3 className="font-serif text-2xl font-semibold text-gray-800 mb-4 mt-8">Why 2025 Is Perfect for Beginners</h3>
              <p className="text-gray-600 leading-relaxed mb-4">
                Here's some good news: nail trends have completely shifted. A few years ago, everyone wanted intricate salon art with rhinestones and 3D details. Now? The biggest trend is minimalism.
              </p>
              <p className="text-gray-600 leading-relaxed mb-4">
                Simple designs are actually what's cool right now. Clean lines, negative space, one accent nail, tiny dots—all the easiest beginner techniques are exactly what's trending. You're not settling for "beginner designs." You're literally doing what professional nail artists are charging $60+ for at salons.
              </p>
              <p className="text-gray-600 leading-relaxed">
                Glass nails, aura nails, soap nails—these viral 2025 trends are easier than traditional nail art. We'll cover exactly how to do them later in this guide using stuff from your makeup bag.
              </p>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 2: Essential Supplies */}
            <div id="supplies" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                🛠️ What You Actually Need to Start
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                Before we get into designs, let's talk supplies. Here's what you need (spoiler: you probably have most of this already).
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <div>
                  <img
                    src="/nail-art-household-tools-toothpick-bobby-pin-tape-sponge.jpg"
                    alt="Household items that work as nail art tools including toothpicks, bobby pins, tape, and makeup sponges"
                    width={600}
                    height={400}
                    className="rounded-2xl shadow-lg w-full"
                  />
                </div>
                <div className="space-y-4">
                  <h3 className="font-serif text-xl font-semibold text-gray-800 mb-4">The Bare Minimum (Need These)</h3>
                  <div className="space-y-3">
                    <div className="flex items-start">
                      <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                      <div>
                        <strong className="text-gray-800">Base coat:</strong>
                        <span className="text-gray-600"> Protects your nails from staining. Not optional. Any drugstore brand works ($4-8).</span>
                      </div>
                    </div>
                    <div className="flex items-start">
                      <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                      <div>
                        <strong className="text-gray-800">2-3 nail polish colors:</strong>
                        <span className="text-gray-600"> Start with contrasting shades like white + navy, or nude + gold. High contrast makes designs visible ($3-5 each).</span>
                      </div>
                    </div>
                    <div className="flex items-start">
                      <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                      <div>
                        <strong className="text-gray-800">Top coat:</strong>
                        <span className="text-gray-600"> Seals everything and makes it last. Also adds shine. Essie or Sally Hansen work great ($5-8).</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <h3 className="font-serif text-2xl font-semibold text-gray-800 mb-6">Household Items You Already Own</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-pink-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">🦷</span>
                  </div>
                  <h4 className="font-semibold text-gray-800 mb-3">Toothpicks</h4>
                  <ul className="text-sm text-gray-600 space-y-2">
                    <li>• <strong>For:</strong> Dots (both ends give different sizes), dragging marble effects, swirls, tiny details</li>
                    <li>• <strong>Pro tip:</strong> Use the pointed end for small dots, blunt end for bigger ones</li>
                    <li>• <strong>Cost:</strong> $0 (you have these)</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">📎</span>
                  </div>
                  <h4 className="font-semibold text-gray-800 mb-3">Bobby Pins</h4>
                  <ul className="text-sm text-gray-600 space-y-2">
                    <li>• <strong>For:</strong> Perfect double dots, easy heart shapes (press twice), larger dots</li>
                    <li>• <strong>Pro tip:</strong> The round end is ideal for uniform dot sizes</li>
                    <li>• <strong>Cost:</strong> $0 (everyone has these)</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">📏</span>
                  </div>
                  <h4 className="font-semibold text-gray-800 mb-3">Scotch Tape or Striping Tape</h4>
                  <ul className="text-sm text-gray-600 space-y-2">
                    <li>• <strong>For:</strong> Clean lines, stripes, French tips, color blocking, geometric designs</li>
                    <li>• <strong>Pro tip:</strong> Regular scotch tape works perfectly. Striping tape ($3) makes even cleaner lines but isn't necessary</li>
                    <li>• <strong>Cost:</strong> $0-3</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">🧽</span>
                  </div>
                  <h4 className="font-semibold text-gray-800 mb-3">Makeup Sponge</h4>
                  <ul className="text-sm text-gray-600 space-y-2">
                    <li>• <strong>For:</strong> Ombre gradients, aura nails, glitter fades, any blended look</li>
                    <li>• <strong>Pro tip:</strong> Cut a makeup wedge sponge into smaller pieces so you can use fresh sections</li>
                    <li>• <strong>Cost:</strong> $0 (use old makeup sponges)</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">💧</span>
                  </div>
                  <h4 className="font-semibold text-gray-800 mb-3">Cotton Swabs + Acetone</h4>
                  <ul className="text-sm text-gray-600 space-y-2">
                    <li>• <strong>For:</strong> Cleaning up messy edges, fixing mistakes, removing polish from skin</li>
                    <li>• <strong>Pro tip:</strong> Dip in acetone, squeeze out excess, then carefully clean around nails</li>
                    <li>• <strong>Cost:</strong> $0 (everyone has these)</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">✏️</span>
                  </div>
                  <h4 className="font-semibold text-gray-800 mb-3">Pencil Eraser (Optional)</h4>
                  <ul className="text-sm text-gray-600 space-y-2">
                    <li>• <strong>For:</strong> Large, uniform dots that are bigger than bobby pin dots</li>
                    <li>• <strong>Pro tip:</strong> Works great for polka dot patterns that need consistent sizing</li>
                    <li>• <strong>Cost:</strong> $0</li>
                  </ul>
                </div>
              </div>

              <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-2xl p-8 border-l-4 border-burgundy-600">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-burgundy-600 rounded-xl flex items-center justify-center flex-shrink-0">
                    <span className="text-2xl">💰</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-gray-900 mb-2 text-lg">Budget Breakdown</h4>
                    <p className="text-gray-700 mb-3">
                      If you're starting completely from scratch: Base coat ($6) + 2 polishes ($6) + Top coat ($6) = $18 total. Everything else you already own.
                    </p>
                    <p className="text-gray-700">
                      Compare that to one salon manicure ($25-40) or a set of gel nails ($50-80). You'll break even after your first at-home design and have supplies for dozens more.
                    </p>
                  </div>
                </div>
              </div>

              <h3 className="font-serif text-2xl font-semibold text-gray-800 mb-6 mt-8">Helpful But Not Essential</h3>
              <p className="text-gray-600 leading-relaxed mb-4">
                Once you're comfortable with basics and want to level up, consider these. But seriously, don't buy them yet. Master the household item designs first.
              </p>
              <ul className="space-y-3 text-gray-600">
                <li className="flex items-start">
                  <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                  <div><strong>Cleanup brush:</strong> Small brush for acetone cleanup (makes edges cleaner) - $3-5</div>
                </li>
                <li className="flex items-start">
                  <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                  <div><strong>Actual dotting tool:</strong> Comes in a set with different sizes - $5-8</div>
                </li>
                <li className="flex items-start">
                  <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                  <div><strong>Striping brush:</strong> Thin brush for lines (toothpicks work fine though) - $3-6</div>
                </li>
                <li className="flex items-start">
                  <span className="w-2 h-2 bg-burgundy-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                  <div><strong>Practice nail tips or wheels:</strong> For trying designs before your real nails - $8-12</div>
                </li>
              </ul>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 3: Nail Prep 101 */}
            <div id="nail-prep" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                💅 Nail Prep 101: The 5-Minute Foundation
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-6">
                Quick heads up: nail prep isn't optional. Skip this and your beautiful design will chip off tomorrow. Do this and it'll last a week. Takes 5 minutes max.
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <div>
                  <img
                    src="/nail-art-prep-clean-file-buff-cuticles.jpg"
                    alt="Nail preparation steps showing cleaned filed buffed nails with pushed back cuticles"
                    width={600}
                    height={400}
                    className="rounded-2xl shadow-lg w-full"
                  />
                </div>
                <div className="space-y-6">
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Step 1: Clean Your Nails</h3>
                    <p className="text-gray-600 text-sm">
                      Wash hands with soap. Remove any old polish completely. Oils on your nails = polish won't stick. That's it.
                    </p>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Step 2: Shape Your Nails</h3>
                    <p className="text-gray-600 text-sm">
                      File in one direction (not back and forth—that causes splitting). Pick any shape you want. Short nails work perfectly for every design in this guide.
                    </p>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Step 3: Deal With Cuticles</h3>
                    <p className="text-gray-600 text-sm">
                      Push them back gently with a wooden stick or your fingernail. Never cut them (infection risk). This creates a smooth base for polish application. Check out our <a href="https://mirelleinspo.com/topics/nail-care-guide" style={{color: '#2563eb', textDecoration: 'underline'}}>nail care guide</a> for more on this.
                    </p>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Step 4: Lightly Buff Surface</h3>
                    <p className="text-gray-600 text-sm">
                      Gently buff the nail surface to remove ridges. Don't go crazy—you're just smoothing, not removing layers. This helps polish adhere better.
                    </p>
                  </div>
                </div>
              </div>

              <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl p-8 border-l-4 border-blue-600 my-8">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-blue-600 rounded-xl flex items-center justify-center flex-shrink-0">
                    <span className="text-2xl">⚠️</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-gray-900 mb-2 text-lg">This Part's Important</h4>
                    <p className="text-gray-700">
                      Base coat isn't just polish. It's a protective layer that prevents dark colors from staining your nails yellow and creates a smooth surface for your design. Apply one thin layer and let it dry 2 minutes before adding color. Non-negotiable.
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 4: ULTRA EASY DESIGNS */}
            <div id="ultra-easy" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                ⭐ Ultra Easy Designs: Start Here!
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                These five designs are where everyone should start. No exceptions. They teach you basic polish application, tool control, and color coordination without requiring any precision. Your first attempt will look good.
              </p>

              {/* Design 1: Single Color Perfection */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Single Color Perfection</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 5 min</span>
                      <span>🛠️ Just polish</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Before you try any nail art, you need to master applying regular polish smoothly. This isn't boring—it's literally the foundation for everything else.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat</li>
                    <li>• One nail polish color (any shade you like)</li>
                    <li>• Top coat</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Seal with top coat</strong></p>
                      <p className="text-gray-600 text-sm">Same three strokes. Cap the tip (swipe across the very edge) to prevent chipping. Let dry 5 minutes before touching anything.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> If you see bubbles, you're applying too thick or shaking the bottle (never shake—roll it between your palms). If it's streaky, you need a second thin coat, not one thick one.
                  </p>
                </div>

                <img
                  src="/nail-art-single-color-perfect-application-technique.jpg"
                  alt="Single color nail polish perfect application showing three stroke method for smooth finish"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto mt-6"
                />
              </div>

              {/* Design 2: Simple Glitter Tips */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">2️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Simple Glitter Tips</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 8 min</span>
                      <span>🛠️ Makeup sponge</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Add sparkle to your tips only. Forgiving because glitter hides imperfect application. Looks way fancier than the effort required.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + solid color polish + glitter polish</li>
                    <li>• Small piece of makeup sponge</li>
                    <li>• Top coat</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base color</strong></p>
                      <p className="text-gray-600 text-sm">Follow the single color method above. Let it dry completely—like actually dry, not just "feels dry." Give it 3-4 minutes.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply glitter to sponge</strong></p>
                      <p className="text-gray-600 text-sm">Paint glitter polish onto a small piece of makeup sponge. You want it saturated but not dripping.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Dab onto nail tips</strong></p>
                      <p className="text-gray-600 text-sm">Gently press the sponge onto just the tips of your nails (about 1/4 to 1/3 of the way down). The sponge creates a gradient effect automatically. Dab don't swipe.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Build up sparkle</strong></p>
                      <p className="text-gray-600 text-sm">Repeat the dabbing 2-3 times for more intense glitter. Let dry between dabs. Seal with top coat.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> This looks especially good for <a href="https://mirelleinspo.com/blog/wedding-nail-designs" style={{color: '#2563eb', textDecoration: 'underline'}}>wedding nails</a> or <a href="https://mirelleinspo.com/blog/new-year-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}}>New Year's celebrations</a>. Nude base with gold glitter tips = instant elegance.
                  </p>
                </div>

                <img
                  src="/nail-art-glitter-tips-sponge-gradient-method.jpg"
                  alt="Glitter tips nail design using makeup sponge showing gradient effect application"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 3: One-Finger Accent Nail */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">3️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">One-Finger Accent Nail</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 10 min</span>
                      <span>🛠️ Just polish</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  This is literally the easiest way to make your nails look intentional and styled. Paint most nails one color, make your ring finger a different color. That's it. Super popular in 2025 minimalist trends.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + 2 contrasting polish colors + top coat</li>
                    <li>• That's literally it</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint 4 nails your main color</strong></p>
                      <p className="text-gray-600 text-sm">On each hand, paint thumb, pointer, middle, and pinky with your base color. Use the single color method. Let dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint ring finger the accent color</strong></p>
                      <p className="text-gray-600 text-sm">On both hands, paint just the ring finger a contrasting color. This is your statement nail. Top coat everything.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm mb-2">
                    <strong>💡 Pro tip:</strong> Color combos that work every time:
                  </p>
                  <ul className="text-gray-700 text-sm space-y-1">
                    <li>• Nude + burgundy</li>
                    <li>• White + navy</li>
                    <li>• Black + gold</li>
                    <li>• Light pink + deep red</li>
                    <li>• Cream + forest green</li>
                  </ul>
                </div>

                <p className="text-gray-600 text-sm mb-4">
                  This design is perfect if you want something that looks put-together but need to do it quickly. Also great for testing new colors—if you're not sure about a shade, try it as an accent nail first. Check out more color matching tips in our <a href="https://mirelleinspo.com/topics/skin-tones" style={{color: '#2563eb', textDecoration: 'underline'}}>skin tones guide</a>.
                </p>

                <img
                  src="/nail-art-one-finger-accent-nail-ring-finger.jpg"
                  alt="One finger accent nail design showing ring finger in contrasting color for minimalist look"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 4: Half & Half Color Block */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">4️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Half & Half Color Block</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 12 min</span>
                      <span>🛠️ Tape</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Two colors split down the middle. The tape does all the work for you, creating a perfectly straight line. Looks geometric and modern with zero artistic skill needed.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + 2 contrasting colors + top coat</li>
                    <li>• Scotch tape or striping tape</li>
                    <li>• Scissors</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint first color all over</strong></p>
                      <p className="text-gray-600 text-sm">Apply your first color to the entire nail. Let it dry completely—this is important. If it's not fully dry, the tape will pull it off. Wait 5 minutes to be safe.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Place tape diagonally or straight</strong></p>
                      <p className="text-gray-600 text-sm">Cut a small piece of tape and place it across your nail where you want the split. Diagonal looks cool. Straight horizontal works too. Press down the edges so no polish bleeds under.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint second color on exposed half</strong></p>
                      <p className="text-gray-600 text-sm">Carefully paint your second color on the section not covered by tape. You can go over the tape edges slightly—that's fine.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Remove tape immediately</strong></p>
                      <p className="text-gray-600 text-sm">While the second color is still wet, gently peel off the tape at an angle. This creates a clean line. If you wait until it dries, it might peel up polish. Top coat once fully dry.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-red-50 to-orange-50 rounded-xl p-6 border-l-4 border-red-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>⚠️ Common mistake:</strong> Removing the tape after the polish dries. Always peel it off while the top layer is still wet. This prevents the polish from cracking or pulling up with the tape.
                  </p>
                </div>

                <img
                  src="/nail-art-half-half-color-block-tape-method.jpg"
                  alt="Half and half color block nail design using tape for clean straight line division"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 5: Random Dots */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">5️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Random Dots</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 10 min</span>
                      <span>🛠️ Toothpick</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  The most forgiving design in existence. Scatter dots randomly across your nails. There's literally no pattern to mess up. Mistakes look intentional. This is where you learn toothpick control without pressure.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + base color + accent color for dots + top coat</li>
                    <li>• Toothpick</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base color</strong></p>
                      <p className="text-gray-600 text-sm">Paint all nails with your base color. Let it dry completely—5 minutes minimum. You're going to be touching the surface with a toothpick so it needs to be fully set.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Dip toothpick in polish</strong></p>
                      <p className="text-gray-600 text-sm">Dip the pointed end of a toothpick into your accent color polish. You want a small bead of polish on the tip.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Press onto nail</strong></p>
                      <p className="text-gray-600 text-sm">Gently press the toothpick onto your nail surface. The polish will transfer, creating a dot. Don't drag—just press and lift. Redip after every 2-3 dots.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Scatter dots randomly</strong></p>
                      <p className="text-gray-600 text-sm">Add dots wherever feels right. No pattern needed. Some nails can have more, some less. Varying the spacing makes it look more organic and artistic. Top coat when dots are dry.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Quick Takeaway:</strong> This design is perfect for practicing dot placement without worrying about messing up a pattern. Once you're comfortable with toothpick control here, you can move to structured polka dots or floral designs. This teaches the fundamental skill of consistent pressure and polish transfer.
                  </p>
                </div>

                <img
                  src="/nail-art-random-dots-scattered-toothpick-technique.jpg"
                  alt="Random scattered dots nail design using toothpick showing forgiving placement pattern"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />

                <p className="text-gray-600 text-sm mt-4">
                  Works beautifully for <a href="https://mirelleinspo.com/blog/valentine-nails-2026" style={{color: '#2563eb', textDecoration: 'underline'}}>Valentine's nails</a> (pink dots on red base) or <a href="https://mirelleinspo.com/blog/winter-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}}>winter designs</a> (white dots on navy = snowfall effect).
                </p>
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* CHECKPOINT: Ultra Easy Designs Complete - Moving to Super Easy Designs */}

            {/* Section 5: SUPER EASY DESIGNS */}
            <div id="super-easy" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                ✨ Super Easy Designs: Level Up
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                You've mastered the basics. These seven designs add one new skill at a time—patterned dots, tape techniques, or simple blending. Still totally doable, just slightly fancier.
              </p>

              {/* Design 6: Classic Polka Dots */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">6️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Classic Polka Dots</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 12 min</span>
                      <span>🛠️ Toothpick or bobby pin</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Same as random dots, but now you're placing them in an organized pattern. Grid layout, diagonal lines, or clustered groups all work. This teaches you to plan placement while using the same toothpick technique you just learned.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + base color + dot color + top coat</li>
                    <li>• Toothpick or bobby pin (bobby pin creates uniform larger dots)</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Plan your pattern</strong></p>
                      <p className="text-gray-600 text-sm">Decide: evenly spaced grid, diagonal rows, or clustered at the tip? Look at the example photo. Start simple—a basic grid of 4-6 dots per nail is perfect for learning.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Create first row of dots</strong></p>
                      <p className="text-gray-600 text-sm">Using the toothpick method from Design 5, place your first row of dots. Try to space them evenly but don't stress if they're slightly off—it still looks cute.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Add remaining rows</strong></p>
                      <p className="text-gray-600 text-sm">Continue your pattern across the nail. Step back between rows to check spacing. Remember: slightly imperfect dots look handmade and charming, not messy.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Let dry and seal</strong></p>
                      <p className="text-gray-600 text-sm">Let dots dry 2-3 minutes before top coat. Top coat will smooth everything out and make the dots look more integrated with the base.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> Use the blunt end of a toothpick or a bobby pin head for larger, more uniform dots. Pointed end for tiny dots. Mixing sizes adds visual interest—try large dots on ring finger, small dots on the rest.
                  </p>
                </div>

                <img
                  src="/nail-art-polka-dots-toothpick-technique-tutorial.jpg"
                  alt="Classic polka dot nail art using toothpick showing evenly spaced dot pattern technique"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 7: Simple French Tips */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">7️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Simple French Tips</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 15 min</span>
                      <span>🛠️ Tape</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  The classic. The tape method makes this way easier than freehand. You're creating that iconic white-tipped look that never goes out of style.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + sheer pink or nude polish + white polish + top coat</li>
                    <li>• Scotch tape or special French tip guides (scotch tape works fine)</li>
                    <li>• Scissors</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply pink/nude base</strong></p>
                      <p className="text-gray-600 text-sm">Paint all nails with sheer pink or nude polish. This creates the natural nail bed look. Two thin coats. Let dry completely—seriously, wait a full 5 minutes. If the base isn't dry, the tape will ruin it.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Place tape for smile line</strong></p>
                      <p className="text-gray-600 text-sm">Cut small pieces of tape. Place them across your nail where you want the white tips to start. The curve should follow your nail's natural curve. Press down the edges firmly.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint white tips</strong></p>
                      <p className="text-gray-600 text-sm">Carefully paint white polish over the exposed tip area. It's okay to go over the tape edges. Use 2 coats for opacity. Don't worry about perfection—the tape is doing the hard work.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Remove tape while wet</strong></p>
                      <p className="text-gray-600 text-sm">Before the white polish dries, gently peel off the tape at an angle. This reveals a clean smile line. If you see any rough edges, clean them up with a cotton swab dipped in acetone. Top coat everything once dry.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border-l-4 border-blue-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>🔬 Why this works:</strong> The tape creates a barrier so you don't have to paint a perfect curve freehand. Even if your white polish application is sloppy, the tape ensures the line is clean. This is why tape is your best friend as a beginner.
                  </p>
                </div>

                <img
                  src="/nail-art-simple-french-tips-tape-method-beginner.jpg"
                  alt="Simple French tip manicure using scotch tape guide for clean white smile line"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 8: Vertical Stripes */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">8️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Vertical Stripes</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 15 min</span>
                      <span>🛠️ Striping tape</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Clean, modern lines that make your nails look longer. Striping tape does all the work—you just press it down. This is basically the adult version of stickers, except way chicer.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + base color + top coat</li>
                    <li>• Striping tape in gold, silver, or contrasting color ($3 at any beauty supply)</li>
                    <li>• Small scissors or nail clippers</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base color</strong></p>
                      <p className="text-gray-600 text-sm">Paint all nails with your base color. Let dry completely. This is your canvas. Any color works but lighter shades make the stripes pop more.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Cut tape to nail length</strong></p>
                      <p className="text-gray-600 text-sm">Peel off a strip of striping tape. Cut pieces slightly longer than your nails. You'll trim the excess after placing them.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Place stripes vertically</strong></p>
                      <p className="text-gray-600 text-sm">Starting at the base of your nail, press down a stripe of tape and smooth it to the tip. Add 1-3 stripes per nail depending on nail width. They can be evenly spaced or asymmetrical—both look good.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Trim and seal</strong></p>
                      <p className="text-gray-600 text-sm">Use scissors or fold the tape over your nail tip and file off the excess. Press down all edges. Apply top coat over everything to seal the stripes and keep them from peeling.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> Gold striping tape on burgundy or navy base = instant sophistication. Silver on black = edgy. White tape on pastels = soft and feminine. This design is especially great for <a href="https://mirelleinspo.com/blog/christmas-nail-designs-2025" style={{color: '#2563eb', textDecoration: 'underline'}}>Christmas nails</a> with red and gold.
                  </p>
                </div>

                <img
                  src="/nail-art-vertical-stripes-striping-tape-application.jpg"
                  alt="Vertical stripe nail design using striping tape for clean modern lines"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 9: Glitter Gradient */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">9️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Glitter Gradient</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 12 min</span>
                      <span>🛠️ Makeup sponge</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Like Design 2 but you're taking it further down the nail for a full gradient effect. The sponge naturally creates that fade—no blending skills required.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + solid color + glitter polish + top coat</li>
                    <li>• Makeup sponge (cut into small pieces)</li>
                    <li>• Cotton swab + acetone for cleanup</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply solid base</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with your base color. This should complement the glitter—try nude with gold glitter, or navy with silver glitter. Dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Load sponge with glitter</strong></p>
                      <p className="text-gray-600 text-sm">Paint glitter polish onto your sponge piece. You want it saturated. The sponge absorbs polish so be generous.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Dab from tip downward</strong></p>
                      <p className="text-gray-600 text-sm">Press the sponge onto your nail tip, then dab it down toward the middle of your nail. Use a gentle bouncing motion. The glitter will be dense at the tip and gradually fade out. Repeat 2-3 times for intensity.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Clean up and seal</strong></p>
                      <p className="text-gray-600 text-sm">Glitter gets messy. Use a cotton swab with acetone to clean up glitter on your skin. Let everything dry, then apply a thick layer of top coat to smooth out the glitter texture.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> This design is perfect for <a href="https://mirelleinspo.com/blog/new-year-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}}>New Year's Eve</a> or any party. The gradient catches light beautifully. For extra dimension, use a chunky glitter over a fine glitter base.
                  </p>
                </div>

                <img
                  src="/nail-art-glitter-gradient-sponge-fade-technique.jpg"
                  alt="Glitter gradient nail design using makeup sponge for ombre sparkle effect"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 10: Ombre Two-Tone */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">🔟</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Ombre Two-Tone</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 15 min</span>
                      <span>🛠️ Makeup sponge</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Two colors blending into each other. Sounds complicated but the sponge does all the blending work. You're just dabbing colors next to each other and the sponge texture creates that professional gradient.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + 2 complementary colors + top coat</li>
                    <li>• Makeup sponge</li>
                    <li>• Small piece of paper or plastic to use as palette</li>
                    <li>• Cotton swab + acetone</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint sponge with both colors</strong></p>
                      <p className="text-gray-600 text-sm">On a piece of paper, paint a thick stripe of your first color. Next to it (slightly overlapping), paint a stripe of your second color. The overlap is where they'll blend.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Pick up with sponge</strong></p>
                      <p className="text-gray-600 text-sm">Press your makeup sponge onto the two color stripes so it picks up both. The sponge should have one color on one side, the other color on the other side, with blending in the middle.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Dab onto nail</strong></p>
                      <p className="text-gray-600 text-sm">Press the sponge onto your nail using a gentle dabbing motion. The colors will transfer with a natural gradient between them. Repeat 2-3 times, reloading the sponge each time for better color saturation.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Clean and top coat</strong></p>
                      <p className="text-gray-600 text-sm">This gets messy on your skin. Clean up with acetone on a cotton swab. Once dry, apply thick top coat to smooth the texture and intensify the colors.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-red-50 to-orange-50 rounded-xl p-6 border-l-4 border-red-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>⚠️ Common issue:</strong> First attempt looks too faint. That's normal—the sponge absorbs a lot of polish. Just reload and dab 2-3 times. Each layer intensifies the color. Also, top coat makes a huge difference in vibrancy.
                  </p>
                </div>

                <img
                  src="/nail-art-ombre-two-tone-sponge-blend-gradient.jpg"
                  alt="Two tone ombre nail design using sponge technique for color gradient blend"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />

                <p className="text-gray-600 text-sm mt-4">
                  Beautiful color combos: pink to purple, blue to teal, peach to coral, nude to burgundy. For seasonal inspiration, check out <a href="https://mirelleinspo.com/topics/seasonal-trends" style={{color: '#2563eb', textDecoration: 'underline'}}>trending seasonal palettes</a>.
                </p>
              </div>

              {/* Design 11: Tiny Hearts */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣1️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Tiny Hearts</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 10 min</span>
                      <span>🛠️ Bobby pin</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  This is a game-changer. Press a bobby pin twice at an angle and boom—perfect heart shape. No drawing required. The trick is all in the angle of the second press.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + base color + accent color for hearts + top coat</li>
                    <li>• Bobby pin</li>
                    <li>• Paper to practice on first</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Practice on paper first</strong></p>
                      <p className="text-gray-600 text-sm">Seriously, try this on paper before your nails. Dip bobby pin in polish, make one dot. Then angle it about 45 degrees and make a second dot touching the first. That's your heart. Practice until you get the angle right.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base color to nails</strong></p>
                      <p className="text-gray-600 text-sm">Paint all nails with your base color. Let dry completely. You need a stable surface for the bobby pin technique.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Create hearts on nails</strong></p>
                      <p className="text-gray-600 text-sm">Dip bobby pin in polish. Make first dot. Without redipping, angle 45 degrees and make second dot touching the first. The two dots form a heart. Scatter 2-4 hearts per nail or do one accent heart on ring finger only.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Let dry and seal</strong></p>
                      <p className="text-gray-600 text-sm">Let hearts dry for 2 minutes before top coat. The top coat will smooth them and make them look more integrated.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Quick Takeaway:</strong> This is the viral TikTok hack that everyone's using. Once you nail the angle (pun intended), you can make perfect hearts in seconds. Perfect for <a href="https://mirelleinspo.com/blog/valentine-nails-2026" style={{color: '#2563eb', textDecoration: 'underline'}}>Valentine's Day</a> or adding a cute touch to any manicure.
                  </p>
                </div>

                <img
                  src="/nail-art-tiny-hearts-bobby-pin-technique-tutorial.jpg"
                  alt="Tiny heart nail design using bobby pin double dot press method tutorial"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 12: Simple Floral (5-Dot Flower) */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣2️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Simple Floral: 5-Dot Flower</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 12 min</span>
                      <span>🛠️ Toothpick</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  The viral TikTok flower with 45M views. Five dots in a circle, one center dot. That's it. Looks like you spent an hour when it takes 2 minutes per nail.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + base color + 2 accent colors (petals + center) + top coat</li>
                    <li>• Toothpick</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base and let dry</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with your base color. Soft colors like pink, mint, or lavender work beautifully. Dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Make 5 dots in circle pattern</strong></p>
                      <p className="text-gray-600 text-sm">Using your petal color and a toothpick, make 5 dots arranged in a circle. They should be touching or very close. The pattern looks like a flower viewed from above. Place 1-2 flowers per nail.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Add center dot</strong></p>
                      <p className="text-gray-600 text-sm">Using a contrasting color (like yellow or white), add one dot in the center of your 5-dot circle. This is the flower center and completes the design.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Optional: Add leaves</strong></p>
                      <p className="text-gray-600 text-sm">If you want to get fancy, add two small green dots next to the flower as leaves. Totally optional. Top coat when dry.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> This design went viral because it's genuinely easy but looks detailed. White petals with yellow center on light blue = daisy vibes. Pink petals with red center on nude = cherry blossom aesthetic. Perfect for spring and <a href="https://mirelleinspo.com/blog/wedding-nail-designs" style={{color: '#2563eb', textDecoration: 'underline'}}>wedding season</a>.
                  </p>
                </div>

                <img
                  src="/nail-art-five-dot-flower-toothpick-floral-tutorial.jpg"
                  alt="Five dot flower nail design using toothpick technique showing viral TikTok floral pattern"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* CHECKPOINT: Super Easy Designs Complete - Moving to Still Easy Designs */}

            {/* Section 6: STILL EASY DESIGNS */}
            <div id="still-easy" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                💫 Still Easy Designs: Building Confidence
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                You're getting comfortable now. These six designs combine techniques you've already learned. They look more advanced but use the same basic skills—just in new ways.
              </p>

              {/* Design 13: Negative Space Lines */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣3️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Negative Space Lines</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 15 min</span>
                      <span>🛠️ Tape</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Leaving parts of your nail bare (negative space) is super trendy right now. Use tape to create geometric sections, paint some areas, leave others clear. Modern and minimalist.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + 1-2 polish colors + top coat</li>
                    <li>• Striping tape or scotch tape</li>
                    <li>• Scissors</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base coat only</strong></p>
                      <p className="text-gray-600 text-sm">Apply clear base coat to bare nails. Let dry. You're keeping the natural nail visible as part of the design.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Create tape pattern</strong></p>
                      <p className="text-gray-600 text-sm">Place tape strips diagonally, horizontally, or in triangles across your nail. This creates sections. The areas under tape will stay clear. Get creative with placement.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint exposed sections</strong></p>
                      <p className="text-gray-600 text-sm">Paint over the areas not covered by tape. You can use one color or multiple. Let dry 30 seconds.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Remove tape while wet</strong></p>
                      <p className="text-gray-600 text-sm">Carefully peel off tape while polish is still wet. This reveals clean lines with negative space. Top coat everything including the bare nail areas.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border-l-4 border-blue-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>🔬 Why this is easy:</strong> The negative space means less area to paint, so fewer opportunities for mistakes. Plus, the geometric look reads as intentional and artistic even if your lines aren't perfect. This is peak minimalist 2025 aesthetic.
                  </p>
                </div>

                <img
                  src="/nail-art-negative-space-lines-geometric-tape.jpg"
                  alt="Negative space line nail design using tape for modern minimalist geometric look"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 14: Confetti Nails */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣4️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Confetti Nails</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 10 min</span>
                      <span>🛠️ Toothpick</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Random tiny strokes and dots in multiple colors. This is the ultimate forgiving design because there's literally no pattern. Messy = artistic. Perfect for using up old polish colors.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + neutral base color + 3-5 bright accent colors + top coat</li>
                    <li>• Toothpick</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply neutral base</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with white, cream, or light gray. This makes your confetti colors pop. Dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Add random strokes</strong></p>
                      <p className="text-gray-600 text-sm">Using a toothpick dipped in your first color, make tiny random strokes across your nail. Short lines, small dashes, whatever. No pattern needed. Just scatter them around.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Add more colors</strong></p>
                      <p className="text-gray-600 text-sm">Repeat with 2-4 more colors. Mix in some dots along with the strokes. The more random and chaotic, the better. There's no wrong way to do this.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Seal the chaos</strong></p>
                      <p className="text-gray-600 text-sm">Let everything dry, then top coat. The top coat will smooth out all the different elements and make it look cohesive.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Quick Takeaway:</strong> This is perfect when you want something fun but don't have time for precision. Each nail can look totally different and it's still cohesive. Great for parties, <a href="https://mirelleinspo.com/blog/new-year-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}}>celebrations</a>, or just expressing creativity without rules.
                  </p>
                </div>

                <img
                  src="/nail-art-confetti-nails-random-strokes-colors.jpg"
                  alt="Confetti nail design with random colorful strokes and dots for artistic chaos look"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 15: Marble Effect */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣5️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Marble Effect</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 12 min</span>
                      <span>🛠️ Toothpick</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Looks expensive and complicated. Actually just dragging a toothpick through wet polish. The key is working fast while the polish is still wet enough to swirl.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + white or light gray base + 1-2 marbling colors + top coat</li>
                    <li>• Toothpick</li>
                    <li>• Quick hands (you need to work while polish is wet)</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base color</strong></p>
                      <p className="text-gray-600 text-sm">Paint nail with white or light gray. Let dry completely. This is your marble base.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Add streaks of marbling color</strong></p>
                      <p className="text-gray-600 text-sm">Using your accent color (gray, black, gold, whatever), paint thin random streaks across the nail. Don't cover the whole nail—just add 3-4 irregular lines. Work on one nail at a time.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Drag toothpick through wet polish</strong></p>
                      <p className="text-gray-600 text-sm">Immediately while the streaks are still wet, drag a clean toothpick through them in swirling motions. This blends and feathers the colors creating that marble look. Work fast—you have about 20 seconds before it dries too much.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Let dry and seal</strong></p>
                      <p className="text-gray-600 text-sm">Don't touch the nail until fully dry—marbling is delicate when wet. Once dry, apply top coat to smooth everything and intensify the effect.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-red-50 to-orange-50 rounded-xl p-6 border-l-4 border-red-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>⚠️ This part trips everyone up:</strong> Waiting too long to drag the toothpick. The polish needs to be wet enough to move and blend. If it's already drying, it won't create that smooth marble effect—it'll just look scraped. Speed is key here.
                  </p>
                </div>

                <img
                  src="/nail-art-marble-effect-toothpick-drag-swirl.jpg"
                  alt="Marble effect nail design using toothpick to drag through wet polish creating swirls"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 16: Micro French Tips */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣6️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Micro French Tips</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 15 min</span>
                      <span>🛠️ Thin brush or toothpick</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  The 2025 update to French tips. Instead of thick white tips, you're painting ultra-thin delicate lines. So trendy right now and easier than traditional French because the line is forgiving—it doesn't have to be perfectly curved.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + sheer nude or pink + white or black polish + top coat</li>
                    <li>• Thin brush (polish brush works) or toothpick</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply natural base</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with sheer nude or soft pink. This creates a natural nail look. Dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Paint thin line at tip</strong></p>
                      <p className="text-gray-600 text-sm">Using the brush from your white polish (wipe off excess on bottle rim to thin it) or a toothpick, paint a super thin line across just the very edge of your nail tip. We're talking 1-2mm thick max. It doesn't have to be perfectly curved—slightly irregular looks chic.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Clean up any wobbles</strong></p>
                      <p className="text-gray-600 text-sm">If your line is wobbly, use a cotton swab with acetone to straighten it. The beauty of micro tips is that small imperfections look intentional and handmade.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Seal with top coat</strong></p>
                      <p className="text-gray-600 text-sm">Let dry, then top coat. The minimalism is the whole point—this is peak 2025 elegance.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> Try black micro tips instead of white for an edgy modern vibe. Or alternate white and black tips on different nails. This style works especially well for <a href="https://mirelleinspo.com/topics/modern-women" style={{color: '#2563eb', textDecoration: 'underline'}}>professional settings</a> because it's subtle but still styled.
                  </p>
                </div>

                <img
                  src="/nail-art-micro-french-tips-thin-line-2025-trend.jpg"
                  alt="Micro French tip nail design showing ultra thin delicate line for minimalist 2025 trend"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 17: Aura Nails */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣7️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Aura Nails</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★★☆ Difficulty</span>
                      <span>⏱️ 12 min</span>
                      <span>🛠️ Makeup sponge or eyeshadow</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  The viral 2025 trend that uses eyeshadow! Yes, makeup eyeshadow. You're creating a soft halo of color around your cuticles. Looks mystical, super trendy, and uses stuff you already have.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + light base color + eyeshadow powder (any color) + top coat</li>
                    <li>• Small makeup sponge or cotton swab</li>
                    <li>• Your eyeshadow brush works too</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply light base color</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with white, cream, or very light pastel. This is your canvas. Dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Pick up eyeshadow on sponge</strong></p>
                      <p className="text-gray-600 text-sm">Dip a small piece of makeup sponge (or cotton swab) into your eyeshadow powder. You want a good amount of pigment on there.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Dab around cuticle area</strong></p>
                      <p className="text-gray-600 text-sm">Gently dab the eyeshadow-loaded sponge around your cuticle area and down the sides of your nail. The goal is a soft, blurred halo effect—like an aura emanating from your cuticle. The center of the nail stays lighter.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Seal with top coat</strong></p>
                      <p className="text-gray-600 text-sm">The eyeshadow will look dusty and matte. Top coat transforms it—the powder becomes vibrant and locks in place. Apply a thick layer of top coat to really intensify the color.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Quick Takeaway:</strong> This went viral because it's genuinely innovative and uses makeup most people already own. Purple eyeshadow creates mystical vibes, pink is romantic, blue is ethereal. The blurred effect is automatically forgiving—there's no "wrong" way to blend an aura.
                  </p>
                </div>

                <img
                  src="/nail-art-aura-nails-eyeshadow-technique-2025.jpg"
                  alt="Aura nail design using eyeshadow powder for soft gradient halo effect around cuticles"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>
{/* Design 18: Abstract Minimalist */}
<div className="mb-12">
  <div className="flex items-center gap-3 mb-4">
    <span className="text-3xl">1️⃣8️⃣</span>
    <div>
      <h3 className="font-serif text-2xl font-semibold text-gray-800">Abstract Minimalist</h3>
      <div className="flex gap-4 text-sm text-gray-500 mt-1">
        <span>★★☆ Difficulty</span>
        <span>⏱️ 10 min</span>
        <span>🛠️ Toothpick</span>
      </div>
    </div>
  </div>
  <p className="text-gray-600 leading-relaxed mb-4">
    Random lines and shapes that look intentionally artistic. The secret? There's no pattern, so you literally can't mess it up. Imperfection IS the aesthetic.
  </p>
  
  <div className="bg-gray-50 p-6 rounded-xl mb-4">
    <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
    <ul className="text-gray-600 space-y-1 text-sm">
      <li>• Base coat + neutral base + 1-2 accent colors + top coat</li>
      <li>• Toothpick or thin brush</li>
      <li>• Permission to be imperfect</li>
    </ul>
  </div>

  <div className="space-y-3 mb-4">
    <div className="flex items-start gap-3">
      <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
        1
      </div>
      <div className="flex-1">
        <p className="text-gray-700"><strong>Apply neutral base</strong></p>
        <p className="text-gray-600 text-sm">Paint nails with beige, cream, white, or soft gray. Abstract art needs a clean canvas. Dry completely.</p>
      </div>
    </div>

    <div className="flex items-start gap-3">
      <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
        2
      </div>
      <div className="flex-1">
        <p className="text-gray-700"><strong>Add random lines</strong></p>
        <p className="text-gray-600 text-sm">Using a toothpick or thin brush, draw random thin lines across your nail. Straight, curved, intersecting—whatever feels right. Keep them minimal. 2-3 lines per nail max.</p>
      </div>
    </div>

    <div className="flex items-start gap-3">
      <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
        3
      </div>
      <div className="flex-1">
        <p className="text-gray-700"><strong>Optional: Add tiny shapes</strong></p>
        <p className="text-gray-600 text-sm">Small dots, half circles, tiny triangles. Keep them sparse. The power is in the negative space. Each nail can have a different composition.</p>
      </div>
    </div>

    <div className="flex items-start gap-3">
      <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
        4
      </div>
      <div className="flex-1">
        <p className="text-gray-700"><strong>Embrace imperfection</strong></p>
        <p className="text-gray-600 text-sm">Shaky lines look artistic. Slightly irregular shapes look intentional. This is the one design where "mistakes" actually make it better. Top coat and call it modern art.</p>
      </div>
    </div>
  </div>

  <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
    <p className="text-gray-700 text-sm">
      <strong>💡 Pro tip:</strong> This is the design to try when you're tired or don't have time for precision. Black lines on white base = classic. Gold lines on nude = expensive looking. Use a contrasting color so your lines are visible. Perfect for days when you want to look put together without the effort.
    </p>
  </div>

  <img
    src="/nail-art-abstract-minimalist-random-lines-shapes.jpg"
    alt="Abstract minimalist nail design with random lines and shapes for artistic modern look"
    width={800}
    height={533}
    className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
  />
</div>
              

            <hr className="my-12 border-cream-400" />

            {/* CHECKPOINT: Still Easy Designs Complete - Moving to 2025 Trending Designs */}

            {/* Section 7: TRENDING 2025 BEGINNER-FRIENDLY DESIGNS */}
            <div id="trending-2025" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                🔥 Trending 2025 Beginner-Friendly Designs
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                These four designs are what's hot right now. The best part? They're all easier than traditional nail art. 2025 trends favor simple techniques that look expensive.
              </p>

              {/* Design 19: Glass Nails */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">1️⃣9️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Glass Nails</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 8 min</span>
                      <span>🛠️ High-gloss top coat</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Ultra-glossy, translucent nails that look like glass. The trick is all in the top coat—you need a high-shine gel-like finish. This is actually one of the easiest "advanced" looks.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + sheer translucent polish or very light nude</li>
                    <li>• High-gloss gel-effect top coat (Essie Gel Couture or Sally Hansen Miracle Gel)</li>
                    <li>• Ridge-filling base coat helps create smooth surface</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Start with smooth nails</strong></p>
                      <p className="text-gray-600 text-sm">Glass nails require smooth nail surfaces. Buff gently to remove ridges. Apply ridge-filling base coat. Let dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply sheer color</strong></p>
                      <p className="text-gray-600 text-sm">Use sheer milky pink, nude, or even clear polish. The translucent quality is key for that glass effect. Two thin coats. Dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply high-gloss top coat</strong></p>
                      <p className="text-gray-600 text-sm">This is where the magic happens. Apply a thick layer of gel-effect top coat. The ultra-glossy finish creates that glass-like appearance. Two coats of top coat if needed for maximum shine.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      4
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Let cure fully</strong></p>
                      <p className="text-gray-600 text-sm">Don't touch for 10 minutes. The thick top coat needs time to fully harden. Once set, you'll have that signature mirror-like finish.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border-l-4 border-blue-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>🔬 Why this is perfect for beginners:</strong> There's no design to mess up. You're literally just applying polish smoothly, which you already learned in Design 1. The high-gloss top coat does all the work of making it look expensive and trendy. For healthy nail tips to achieve the best glass nail look, check our <a href="https://mirelleinspo.com/topics/nail-care-guide" style={{color: '#2563eb', textDecoration: 'underline'}}>nail strengthening guide</a>.
                  </p>
                </div>

                <img
                  src="/nail-art-glass-nails-ultra-glossy-translucent-finish.jpg"
                  alt="Glass nail trend showing ultra glossy translucent finish with mirror like shine effect"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 20: Mocha Mousse Solid */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">2️⃣0️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Mocha Mousse Solid</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 5 min</span>
                      <span>🛠️ Just polish</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Pantone's Color of the Year 2025. Warm brown shade that's universally flattering. This isn't a technique—it's literally just painting your nails this specific trendy color. Easy as it gets.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + mocha brown polish (warm medium brown) + top coat</li>
                    <li>• Look for: OPI "You Don't Know Jacques", Essie "Chinchilly", or any warm brown</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply base coat</strong></p>
                      <p className="text-gray-600 text-sm">Standard base coat application. Let dry 2 minutes.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply mocha brown</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with your warm brown shade. Two thin coats for even coverage. This color is so on-trend right now that you don't need any design—the color IS the statement.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Top coat and you're done</strong></p>
                      <p className="text-gray-600 text-sm">That's it. You're literally wearing Pantone's Color of the Year. Instant trendiness with zero effort.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Quick Takeaway:</strong> Sometimes the trend is just about wearing the right color. Mocha mousse is everywhere in 2025—fashion, home decor, and nails. This warm brown complements literally every skin tone, works for any season, and looks sophisticated without trying. Perfect for <a href="https://mirelleinspo.com/topics/modern-women" style={{color: '#2563eb', textDecoration: 'underline'}}>professional settings</a> or everyday wear.
                  </p>
                </div>

                <img
                  src="/nail-art-mocha-mousse-pantone-2025-warm-brown.jpg"
                  alt="Mocha mousse solid nail color Pantone 2025 showing warm brown trendy shade"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 21: Soap Nails */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">2️⃣1️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Soap Nails</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 8 min</span>
                      <span>🛠️ Just polish</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Hailey Bieber's latest obsession. Milky white base with ultra-glossy finish. Clean, minimalist, and gives "expensive skincare routine" energy. Super easy—just white polish + glossy top coat.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + milky white polish (not bright white, softer) + glossy top coat</li>
                    <li>• Try: Essie "Blanc", OPI "Funny Bunny", or any cream white</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply milky white base</strong></p>
                      <p className="text-gray-600 text-sm">Paint nails with soft milky white. Not stark bright white—you want that creamy soap-like opacity. Two-three coats for full coverage. Let dry completely.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply super glossy top coat</strong></p>
                      <p className="text-gray-600 text-sm">The shine is crucial. Apply thick layer of your glossiest top coat. The combination of matte milky white with high gloss creates that soap bar aesthetic. That's the whole look.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-burgundy-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Optional: Keep nails short</strong></p>
                      <p className="text-gray-600 text-sm">Soap nails look best on short-medium length nails. The clean, minimal vibe is enhanced by modest length. Trim if needed before starting.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-xl p-6 border-l-4 border-burgundy-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Pro tip:</strong> This is the ultimate "clean girl" aesthetic nail. Works for literally any occasion. Professional enough for work, chic enough for events, simple enough for everyday. Bonus: any chips or wear blend in better than with dark colors, so it lasts longer looking fresh.
                  </p>
                </div>

                <img
                  src="/nail-art-soap-nails-milky-white-glossy-hailey-bieber.jpg"
                  alt="Soap nail trend showing milky white glossy finish for clean minimalist aesthetic"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>

              {/* Design 22: Jelly Nails */}
              <div className="mb-12">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">2️⃣2️⃣</span>
                  <div>
                    <h3 className="font-serif text-2xl font-semibold text-gray-800">Jelly Nails</h3>
                    <div className="flex gap-4 text-sm text-gray-500 mt-1">
                      <span>★☆☆ Difficulty</span>
                      <span>⏱️ 8 min</span>
                      <span>🛠️ Just polish</span>
                    </div>
                  </div>
                </div>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Translucent, squishy-looking nails in bright colors. The sheer quality is forgiving—it hides application mistakes and nail imperfections. Plus, it's trending hard right now.
                </p>
                
                <div className="bg-gray-50 p-6 rounded-xl mb-4">
                  <h4 className="font-semibold text-gray-800 mb-3">What You Need:</h4>
                  <ul className="text-gray-600 space-y-1 text-sm">
                    <li>• Base coat + jelly polish (sheer translucent formula) + glossy top coat</li>
                    <li>• Look for sheer formulas in pink, coral, blue, green—any bright color</li>
                    <li>• Regular polish applied thin works too</li>
                  </ul>
                </div>

                <div className="space-y-3 mb-4">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      1
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Apply sheer base</strong></p>
                      <p className="text-gray-600 text-sm">If using jelly polish, apply one coat. It should be see-through. If using regular polish, apply ONE very thin coat—you want translucency, not full opacity.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      2
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Build color gradually</strong></p>
                      <p className="text-gray-600 text-sm">Add 1-2 more thin coats to build up the jelly effect. You should still see your nail through the color but it should be vibrant. The translucency is the whole aesthetic.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-pink-600 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0 mt-1">
                      3
                    </div>
                    <div className="flex-1">
                      <p className="text-gray-700"><strong>Glossy finish is essential</strong></p>
                      <p className="text-gray-600 text-sm">Apply thick glossy top coat. The high shine creates that wet, jelly-like appearance. This is what makes it look squishy and fun.</p>
                    </div>
                  </div>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-xl p-6 border-l-4 border-green-600 mb-4">
                  <p className="text-gray-700 text-sm">
                    <strong>💡 Quick Takeaway:</strong> Jelly nails are perfect for summer or fun occasions. The sheer formula is forgiving of streaks or uneven application—it just adds to the dimensional look. Try bright coral for <a href="https://mirelleinspo.com/blog/holiday-vacation-nails-travel-guide" style={{color: '#2563eb', textDecoration: 'underline'}}>vacation vibes</a>, or pastel pink for everyday sweetness.
                  </p>
                </div>

                <img
                  src="/nail-art-jelly-nails-translucent-glossy-bright-color.jpg"
                  alt="Jelly nail trend showing translucent sheer bright color with glossy squishy finish"
                  width={800}
                  height={533}
                  className="rounded-xl shadow-lg w-full max-w-2xl mx-auto"
                />
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* CHECKPOINT: Trending 2025 Designs Complete - Moving to Mistakes Section */}

            {/* Section 8: Common Mistakes & Fixes */}
            <div id="mistakes" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                ❌ 7 Beginner Mistakes & How to Fix Them
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                Everyone makes these mistakes. Seriously, everyone. Here's how to avoid them or fix them when they happen.
              </p>

              <div className="space-y-6">
                {/* Mistake 1 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-red-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">1️⃣</span>
                    Skipping Base Coat or Top Coat
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> Base coat protects from staining and helps polish stick. Top coat seals everything and prevents chipping. Skip them and your design lasts maybe one day before looking terrible.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Just don't skip them. Ever. They're non-negotiable. Budget $6 each for decent drugstore versions and they'll last months. The extra 2 minutes is worth having your nails look good all week instead of one day.
                  </p>
                </div>

                {/* Mistake 2 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-orange-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">2️⃣</span>
                    Not Waiting for Polish to Dry
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> Smudges, dents, or your whole design gets wrecked because you touched something too soon. This is the #1 cause of beginner frustration.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Set a timer. Base coat = 2 minutes. Each polish coat = 2-3 minutes. Top coat = 5 minutes minimum before touching anything. Seriously set a phone timer. Use this time to scroll, not do stuff with your hands. Quick-dry drops help but patience is better.
                  </p>
                </div>

                {/* Mistake 3 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-yellow-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">3️⃣</span>
                    Polish All Over Your Cuticles
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> Makes your manicure look messy and unprofessional. Also peels off faster when polish is on skin instead of nail.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Leave tiny gap between polish and cuticle when applying. Clean up mistakes with cotton swab dipped in acetone. Go slowly around the edges. Practice makes this easier—your first few attempts will be messier and that's fine. Also, petroleum jelly on skin around nails before polishing makes cleanup way easier—the polish won't stick to skin.
                  </p>
                </div>

                {/* Mistake 4 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-green-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">4️⃣</span>
                    Applying Coats Too Thick
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> Thick coats bubble, take forever to dry, and create that goopy texture. They also chip faster because they never fully cure.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Thin coats, multiple layers. Wipe excess polish off the brush on the bottle rim before applying. Two thin coats always beat one thick coat. If polish is goopy, add a drop of nail polish thinner (not acetone—that ruins it). Think light layers that build up color gradually.
                  </p>
                </div>

                {/* Mistake 5 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-blue-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">5️⃣</span>
                    Pressing Too Hard with Tools
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> Dots become blobs, lines become smears, you dent the base polish. Gentle pressure is key but beginners always press too hard out of nervousness.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Practice on paper first to learn the right pressure. For dots, you barely touch the surface—the polish transfers with minimal pressure. For lines, think of guiding the toothpick, not digging with it. Light touch = better control. Take your time.
                  </p>
                </div>

                {/* Mistake 6 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-purple-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">6️⃣</span>
                    Comparing to Professional Results
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> You get discouraged and quit when your first attempts don't look like Instagram posts. Those are done by professionals with years of practice, perfect lighting, and often editing.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Your first nail art won't be perfect and that's completely normal. Compare your attempts to your previous attempts, not to professionals. Celebrate progress. Every design you do teaches you something. Most people need 5-10 practice rounds before designs look really good. That's the learning curve and it's okay.
                  </p>
                </div>

                {/* Mistake 7 */}
                <div className="glass-card p-6 rounded-xl border-l-4 border-pink-500">
                  <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <span className="text-2xl mr-3">7️⃣</span>
                    Giving Up After First Try
                  </h3>
                  <p className="text-gray-600 text-sm mb-3">
                    <strong>Why it's bad:</strong> You miss out on actually getting good at something fun and useful. First attempts at anything new feel awkward.
                  </p>
                  <p className="text-gray-700 text-sm">
                    <strong>Fix:</strong> Commit to trying at least three designs before deciding nail art isn't for you. Your third attempt will be noticeably better than your first. Practice the ultra easy designs until they feel comfortable, then move up. Small improvements add up fast. The satisfaction of creating something beautiful on your own nails is worth pushing through the learning phase.
                  </p>
                </div>
              </div>

              <div className="bg-gradient-to-br from-burgundy-50 to-pink-50 rounded-2xl p-8 border-l-4 border-burgundy-600 mt-8">
                <h3 className="font-bold text-gray-900 mb-3 text-lg">🛠️ Mid-Design Fixes</h3>
                <div className="space-y-3 text-gray-700 text-sm">
                  <p><strong>Smudged before drying?</strong> Let it dry completely, then apply another thin coat over it. The fresh coat will smooth out the smudge.</p>
                  <p><strong>Dot placed wrong?</strong> Immediately wipe it off with clean toothpick while wet, or let it dry and carefully remove with cotton swab dipped in acetone.</p>
                  <p><strong>Polish pooled around cuticles?</strong> Dip cotton swab in acetone, squeeze out excess, and carefully clean up edges while polish is still wet or after it dries.</p>
                  <p><strong>Colors look muddy?</strong> You blended wet colors too much. Let first color dry before adding second color. Work with dry layers, not wet-on-wet unless doing intentional marbling.</p>
                </div>
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 9: Non-Dominant Hand Strategies */}
            <div id="non-dominant" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                🤚 Mastering Your Non-Dominant Hand
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-6">
                Let's address the elephant in the room: your non-dominant hand is going to be harder. Your right hand looks perfect, your left hand looks like a toddler did it. Everyone experiences this.
              </p>

              <p className="text-gray-600 leading-relaxed mb-8">
                Here's the thing—there's no magic trick that makes your non-dominant hand suddenly as coordinated as your dominant hand. But there are strategies that help a lot.
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <div className="glass-card p-6 rounded-xl">
                  <h3 className="font-semibold text-gray-800 mb-4 flex items-center">
                    <span className="text-2xl mr-3">💡</span>
                    Strategy 1: Start Simpler
                  </h3>
                  <p className="text-gray-600 text-sm">
                    Do a slightly simpler version of the design on your non-dominant hand. If your dominant hand has intricate dots, your non-dominant hand can have fewer dots or bigger dots. Both hands don't need to be identical.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <h3 className="font-semibold text-gray-800 mb-4 flex items-center">
                    <span className="text-2xl mr-3">📏</span>
                    Strategy 2: Use More Tape
                  </h3>
                  <p className="text-gray-600 text-sm">
                    Tape-based designs (stripes, French tips, color blocking) are more forgiving on your non-dominant hand because the tape does the precision work. Your shakier hand just needs to fill in sections.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <h3 className="font-semibold text-gray-800 mb-4 flex items-center">
                    <span className="text-2xl mr-3">🎯</span>
                    Strategy 3: Practice More
                  </h3>
                  <p className="text-gray-600 text-sm">
                    Practice designs on paper with your non-dominant hand before trying on nails. Build that muscle memory. Do your non-dominant hand first when you're fresh and not frustrated, or last when you're already committed to finishing.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <h3 className="font-semibold text-gray-800 mb-4 flex items-center">
                    <span className="text-2xl mr-3">✨</span>
                    Strategy 4: Embrace Asymmetry
                  </h3>
                  <p className="text-gray-600 text-sm">
                    Make asymmetry intentional. Each hand can have a different design variation. Or keep non-dominant hand super simple—like solid color or just glitter tips—while dominant hand gets the full design. This is actually a trendy look.
                  </p>
                </div>
              </div>

              <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl p-8 border-l-4 border-blue-600">
                <h4 className="font-bold text-gray-900 mb-2 text-lg">Real Talk</h4>
                <p className="text-gray-700 mb-3">
                  Your non-dominant hand will never look exactly like your dominant hand, especially when you're starting out. That's fine. What matters is that both hands look intentional and styled, not that they're perfectly matched twins.
                </p>
                <p className="text-gray-700">
                  After practicing regularly for a month, your non-dominant hand coordination improves noticeably. It's a skill that develops with repetition. Be patient with yourself.
                </p>
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 10: 2025 Nail Art Trends */}
            <div id="trends" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                🌟 Why 2025 Is the Perfect Year for Beginners
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-6">
                Here's some genuinely good news: nail art trends have completely shifted in your favor. Five years ago, elaborate 3D designs with rhinestones and hand-painted details dominated. Totally intimidating for beginners.
              </p>

              <p className="text-gray-600 leading-relaxed mb-8">
                In 2025? The biggest trends are literally the easiest techniques. Minimalism won. Simple is chic. Natural nails are celebrated. You're not settling for beginner designs—you're doing exactly what's trending.
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">✨</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-3">Minimalist Revival</h3>
                  <p className="text-gray-600 text-sm">
                    Clean lines, negative space, single accent nails, tiny details—all the stuff that's easy for beginners is what's actually cool right now. Complex salon art is considered outdated by trend forecasters.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-pink-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">💅</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-3">Natural Nail Movement</h3>
                  <p className="text-gray-600 text-sm">
                    Healthy natural nails are IN. Short lengths, strengthening treatments, letting nails breathe between manicures—the nail health approach is trending. You don't need long extensions or gels to be stylish.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">🎨</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-3">Imperfection as Art</h3>
                  <p className="text-gray-600 text-sm">
                    Hand-done, slightly imperfect designs are valued over machine-perfect salon work. The "I did this myself" aesthetic is cool. Your shaky lines and irregular dots? Actually on-trend as authentic and artisanal.
                  </p>
                </div>

                <div className="glass-card p-6 rounded-xl">
                  <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
                    <span className="text-2xl">🌿</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-3">DIY & Budget Beauty</h3>
                  <p className="text-gray-600 text-sm">
                    The DIY beauty movement is huge. People want to learn skills, not just pay for services. Creating your own nail art aligns with the broader trend of self-sufficiency and budget consciousness.
                  </p>
                </div>
              </div>

              <p className="text-gray-600 leading-relaxed mb-4">
                The nail designs getting millions of views on TikTok right now? Most are beginner-friendly techniques like the 5-dot flower (45M views), aura nails using eyeshadow, glass nails with just polish, and minimalist line art.
              </p>

              <p className="text-gray-600 leading-relaxed">
                You're literally starting nail art at the perfect time. The techniques trending in 2025 are ones you can master in your first week. Check out more <a href="https://mirelleinspo.com/topics/seasonal-trends" style={{color: '#2563eb', textDecoration: 'underline'}}>seasonal trend updates</a> to stay current with what's popular.
              </p>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 11: Nail Health & Safety */}
            <div id="nail-health" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                🏥 Keeping Your Nails Healthy While Having Fun
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                Nail art is fun but nail health comes first. Here's how to enjoy designing without damaging your natural nails.
              </p>

              <div className="space-y-6 mb-8">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                    <span className="text-xl">✅</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Give Nails Breaks</h3>
                    <p className="text-gray-600 text-sm">
                      Every 2-3 weeks, go polish-free for a few days. This lets nails breathe and recover. During breaks, apply cuticle oil daily and let nails strengthen naturally. Check our <a href="https://mirelleinspo.com/topics/nail-care-guide" style={{color: '#2563eb', textDecoration: 'underline'}}>strengthening guide</a> for detailed tips.
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                    <span className="text-xl">✅</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Remove Polish Properly</h3>
                    <p className="text-gray-600 text-sm">
                      Never peel off polish—this removes layers of your nail with it, causing weakness and peeling. Always use acetone or non-acetone remover. Soak for 30 seconds, then wipe gently. Moisturize immediately after removal.
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                    <span className="text-xl">✅</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Hydrate, Hydrate, Hydrate</h3>
                    <p className="text-gray-600 text-sm">
                      Polish dries out nails. Combat this with cuticle oil daily, especially before bed. Hand cream after every hand washing. Healthy, hydrated nails take polish better and designs last longer.
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                    <span className="text-xl">✅</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Use Acetone-Free When Possible</h3>
                    <p className="text-gray-600 text-sm">
                      Acetone is harsh and drying. For regular polish, acetone-free removers work fine and are gentler. Save acetone for stubborn glitter or when you need something stronger. Always moisturize after using any remover.
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                    <span className="text-xl">✅</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Watch for Warning Signs</h3>
                    <p className="text-gray-600 text-sm">
                      If nails become excessively brittle, yellow, painful, or develop ridges, take a break from polish and see a doctor if it persists. These can indicate underlying health issues or product reactions.
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                    <span className="text-xl">✅</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">Base Coat Protects Against Staining</h3>
                    <p className="text-gray-600 text-sm">
                      Dark colors especially can stain nails yellow without base coat. Always use base coat—it's protection, not optional. If nails do get stained, buff gently with a buffer and give them a week to recover.
                    </p>
                  </div>
                </div>
              </div>

              <div className="bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl p-8 border-l-4 border-red-600">
                <h4 className="font-bold text-gray-900 mb-2 text-lg">⚠️ When to See a Professional</h4>
                <p className="text-gray-700 text-sm mb-3">
                  If you notice persistent pain, swelling around nails, discoloration that won't go away, nails separating from nail bed, or any signs of infection, see a dermatologist or doctor. Don't try to treat nail infections with polish or home remedies.
                </p>
                <p className="text-gray-700 text-sm">
                  Nail health is part of overall health. Take it seriously even though it seems cosmetic.
                </p>
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Section 12: Practice & Progression Path */}
            <div className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8">
                📈 Your Progression Path: From Dots to Detailed
              </h2>
              
              <p className="text-gray-600 leading-relaxed mb-8">
                Here's exactly how to progress your skills over the next month. Don't skip ahead or you'll get frustrated.
              </p>

              <div className="space-y-6">
                <div className="glass-card p-6 rounded-xl border-l-4 border-burgundy-400">
                  <h3 className="font-semibold text-gray-800 mb-3">Week 1: Master the Basics</h3>
                  <ul className="space-y-2 text-gray-600 text-sm">
                    <li>• Try designs 1-5 (Ultra Easy category)</li>
                    <li>• Focus on: smooth polish application, working with toothpicks, using tape</li>
                    <li>• Goal: Feel confident applying polish evenly and making simple dots</li>
                    <li>• Practice each design at least twice</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl border-l-4 border-pink-400">
                  <h3 className="font-semibold text-gray-800 mb-3">Week 2: Add Patterns</h3>
                  <ul className="space-y-2 text-gray-600 text-sm">
                    <li>• Try designs 6-12 (Super Easy category)</li>
                    <li>• Focus on: organized placement, sponge techniques, combining skills</li>
                    <li>• Goal: Create recognizable patterns and use multiple techniques in one design</li>
                    <li>• Start practicing on your non-dominant hand more</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl border-l-4 border-purple-400">
                  <h3 className="font-semibold text-gray-800 mb-3">Week 3: Build Complexity</h3>
                  <ul className="space-y-2 text-gray-600 text-sm">
                    <li>• Try designs 13-18 (Still Easy category)</li>
                    <li>• Focus on: combining multiple techniques, working faster, color theory</li>
                    <li>• Goal: Complete more intricate designs with confidence</li>
                    <li>• Experiment with your own color combinations</li>
                  </ul>
                </div>

                <div className="glass-card p-6 rounded-xl border-l-4 border-blue-400">
                  <h3 className="font-semibold text-gray-800 mb-3">Week 4: Master Trending Looks</h3>
                  <ul className="space-y-2 text-gray-600 text-sm">
                    <li>• Try designs 19-22 (2025 Trending category)</li>
                    <li>• Focus on: perfecting techniques, developing personal style, speed</li>
                    <li>• Goal: Create trendy looks quickly and efficiently</li>
                    <li>• Start creating your own design variations</li>
                  </ul>
                </div>
              </div>

              <div className="bg-gradient-to-br from-green-50 to-teal-50 rounded-2xl p-8 border-l-4 border-green-600 mt-8">
                <h4 className="font-bold text-gray-900 mb-2 text-lg">🎯 Progress Markers</h4>
                <p className="text-gray-700 text-sm mb-3">
                  You'll know you're ready to move to the next week when:
                </p>
                <ul className="space-y-2 text-gray-700 text-sm">
                  <li>• The current week's designs feel comfortable, not stressful</li>
                  <li>• Your second attempt looks noticeably better than your first</li>
                  <li>• You're not making the same mistakes repeatedly</li>
                  <li>• You can complete designs without constantly checking instructions</li>
                  <li>• You're excited to try the next level, not dreading it</li>
                </ul>
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* FAQ Section */}
            <div id="faq" className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8 text-center">
                ❓ Frequently Asked Questions
              </h2>
              
              <p className="text-gray-600 text-center mb-12 max-w-2xl mx-auto">
                The 15 questions every beginner asks. If you're wondering about it, the answer is probably here.
              </p>

              <div className="space-y-4">
                {/* All FAQs with proper structure */}
                {[
                  {
                    q: "How do I start doing nail art as a beginner?",
                    a: "Start with the simplest designs like single color perfection or random dots using household items you already have. Practice basic application first, then progress to easy designs using toothpicks for dots, tape for stripes, and sponges for gradients. Focus on mastering one technique before moving to the next."
                  },
                  {
                    q: "What is the easiest nail design for first timers?",
                    a: "Random dots are the easiest nail design for first-timers because there is no pattern to follow and mistakes look intentional. Use a toothpick dipped in polish to create scattered dots across a base color. This forgiving design builds confidence while teaching basic tool control and color coordination."
                  },
                  {
                    q: "Can I do nail art without any tools?",
                    a: "Yes, you can create beautiful nail art with household items. Use toothpicks for dots and lines, bobby pins for double dots and hearts, scotch tape for stripes, makeup sponges for ombre, and cotton swabs with acetone for cleanup. No special nail art tools are required to start."
                  },
                  {
                    q: "What nail designs are best for beginners?",
                    a: "Best beginner designs include polka dots, simple French tips, vertical stripes with tape, glitter gradients, one-finger accent nails, and basic color blocking. These designs require minimal precision, use simple techniques, and look impressive despite being easy to execute with basic household items."
                  },
                  {
                    q: "How do I make dots on my nails at home?",
                    a: "Dip a toothpick into nail polish and gently press onto your nail surface. For smaller dots, use the pointed end. For larger dots, use the blunt end or a bobby pin head. Let the base color dry completely first. Practice the pressure needed on paper before trying on nails."
                  },
                  {
                    q: "What can I use instead of a dotting tool?",
                    a: "Toothpicks, bobby pins, pencil erasers, ballpoint pen tips, or even the head of a sewing pin make excellent dotting tool substitutes. Bobby pins create perfect double dots for easy designs. Toothpick tips offer varying dot sizes depending on which end you use."
                  },
                  {
                    q: "How do I do simple French tips at home?",
                    a: "Apply a sheer pink or nude base coat first. Let dry completely. Use scotch tape or striping tape to mark the smile line across your nail tip. Paint white polish over the tip area, let dry 30 seconds, then carefully remove tape. Seal with clear top coat for smooth finish."
                  },
                  {
                    q: "What is an easy nail art design for short nails?",
                    a: "Half moon manicure, tiny dots, micro French tips, single accent nail, and vertical stripes all work beautifully on short nails. These designs do not require length to look elegant. Focus on horizontal or minimal patterns that enhance the nail shape rather than require extended canvas space."
                  },
                  {
                    q: "How long does nail art take for beginners?",
                    a: "Simple designs take 5 to 10 minutes per hand for beginners including drying time between steps. Your first attempts may take 15 to 20 minutes as you learn techniques. With practice, most easy designs become faster. Allow 30 minutes total for full manicure including prep, base coat, design, and top coat."
                  },
                  {
                    q: "Can I do nail art with just nail polish?",
                    a: "Yes, you need only nail polish plus household items. Base coat, two or more polish colors, and top coat are essential. Add toothpicks, tape, and sponges you already own. No special brushes, gels, or equipment required. Regular polish works perfectly for all beginner designs in this guide."
                  },
                  {
                    q: "What colors are easiest for nail art beginners?",
                    a: "Start with high-contrast color combinations like black on white, white on navy, or gold on burgundy. These contrasts make designs visible and mistakes less obvious. Avoid sheer or similar-toned colors initially. Nude base with bright accent colors offers forgiving canvas for learning technique."
                  },
                  {
                    q: "How do I keep my hand steady for nail art?",
                    a: "Rest both elbows on a table or firm surface. Work in good lighting. Take breaks if hands get tired or shaky. Practice designs on paper first to build muscle memory. Consider working in short sessions rather than rushing. Caffeine can increase shakiness so avoid before nail art sessions."
                  },
                  {
                    q: "What is the simplest nail design to try first?",
                    a: "Single color perfection is the simplest starting point to master basic polish application. Once comfortable, try random dots with a toothpick which requires no pattern or precision. These foundational skills build confidence before progressing to designs requiring more control like stripes or French tips."
                  },
                  {
                    q: "Do I need special brushes for nail art?",
                    a: "No special brushes are needed for beginner nail art. Use the brush inside your polish bottle for base application. Toothpicks, tape, and sponges create all the designs in this guide. Once you advance, a thin striping brush and cleanup brush are helpful but not essential initially."
                  },
                  {
                    q: "Can I use a toothpick for nail designs?",
                    a: "Toothpicks are perfect for nail art. Use the pointed end for tiny dots and fine lines. Use the blunt end for larger dots. Drag through wet polish to create marble effects, swirls, or floral designs. Toothpicks offer excellent control and precision for beginners at zero cost."
                  }
                ].map((faq, index) => (
                  <details key={index} className="group glass-card rounded-xl border border-gray-200 overflow-hidden hover:border-burgundy-300 transition-colors">
                    <summary className="cursor-pointer px-6 py-5 flex justify-between items-center touch-target">
                      <h3 className="font-semibold text-gray-900 pr-4">{faq.q}</h3>
                      <svg className="w-5 h-5 text-burgundy-600 transform group-open:rotate-45 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                      </svg>
                    </summary>
                    <div className="px-6 pb-5 text-gray-600 leading-relaxed">
                      {faq.a}
                    </div>
                  </details>
                ))}
              </div>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* E-E-A-T Section */}
            <div className="mb-16 bg-gradient-to-br from-cream-50 to-burgundy-50 rounded-2xl p-8">
              <h2 className="font-serif text-2xl font-bold text-gray-900 mb-4">About Mirellé Team</h2>
              <p className="text-gray-600 leading-relaxed mb-4">
                We're nail enthusiasts who test and practice every technique before sharing it with you. Our mission is making nail art accessible for everyone—no intimidation, no gatekeeping, just honest tutorials that actually work for beginners. Every design in this guide has been tested by real beginners to ensure it's truly doable.
              </p>
              <a href="https://mirelleinspo.com/about" style={{color: '#2563eb', textDecoration: 'underline'}} className="font-medium">
                Learn more about our team and approach →
              </a>
            </div>

            <hr className="my-12 border-cream-400" />

            {/* Related Topics */}
            <div className="mb-16">
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-gray-900 mb-8 text-center">
                Keep Learning & Creating
              </h2>
              
              <p className="text-gray-600 text-center mb-12 max-w-2xl mx-auto">
                You've got the basics down. Now explore these related guides to expand your nail skills and find design inspiration.
              </p>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                {/* Related Topic 1 */}
                <Link href="https://mirelleinspo.com/topics/nail-care-guide" className="group">
                  <div className="glass-card p-6 rounded-xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                    <div className="w-12 h-12 bg-pink-100 rounded-lg flex items-center justify-center mb-4">
                      <span className="text-2xl">💅</span>
                    </div>
                    <h3 className="font-serif text-xl font-semibold text-gray-800 mb-3 group-hover:text-burgundy-600 transition-colors">
                      Nail Care & Strengthening
                    </h3>
                    <p className="text-sm text-gray-600 mb-4">
                      Keep your nails healthy and strong with proper care techniques. Essential reading for maintaining the perfect canvas for your nail art designs.
                    </p>
                    <div className="text-xs text-gray-500 flex items-center">
                      <span className="mr-2">📖</span>
                      12-minute read • Health-focused
                    </div>
                  </div>
                </Link>

                {/* Related Topic 2 */}
                <Link href="https://mirelleinspo.com/topics/skin-tones" className="group">
                  <div className="glass-card p-6 rounded-xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                    <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                      <span className="text-2xl">🎨</span>
                    </div>
                    <h3 className="font-serif text-xl font-semibold text-gray-800 mb-3 group-hover:text-burgundy-600 transition-colors">
                      Colors for Your Skin Tone
                    </h3>
                    <p className="text-sm text-gray-600 mb-4">
                      Discover which nail colors complement your skin tone best. Learn color theory that makes choosing polish shades easy and ensures flattering results every time.
                    </p>
                    <div className="text-xs text-gray-500 flex items-center">
                      <span className="mr-2">🌈</span>
                      8-minute read • Color matching
                    </div>
                  </div>
                </Link>

                {/* Related Topic 3 */}
                <Link href="https://mirelleinspo.com/topics/seasonal-trends" className="group">
                  <div className="glass-card p-6 rounded-xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                    <div className="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center mb-4">
                      <span className="text-2xl">🍂</span>
                    </div>
                    <h3 className="font-serif text-xl font-semibold text-gray-800 mb-3 group-hover:text-burgundy-600 transition-colors">
                      Seasonal Nail Trends
                    </h3>
                    <p className="text-sm text-gray-600 mb-4">
                      Stay updated with what's trending each season. From spring florals to winter sparkle, get inspiration for designs that match the current vibe.
                    </p>
                    <div className="text-xs text-gray-500 flex items-center">
                      <span className="mr-2">✨</span>
                      10-minute read • Updated monthly
                    </div>
                  </div>
                </Link>
              </div>

              {/* Additional Blog Links */}
              <div className="mt-12 pt-8 border-t border-cream-400">
                <h3 className="font-serif text-xl font-semibold text-gray-800 mb-6 text-center">
                  Design Inspiration by Occasion
                </h3>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                  <a href="https://mirelleinspo.com/blog/christmas-nail-designs-2025" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Christmas Nails
                  </a>
                  <a href="https://mirelleinspo.com/blog/wedding-nail-designs" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Wedding Designs
                  </a>
                  <a href="https://mirelleinspo.com/blog/valentine-nails-2026" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Valentine's Day
                  </a>
                  <a href="https://mirelleinspo.com/blog/winter-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Winter Nails
                  </a>
                  <a href="https://mirelleinspo.com/blog/new-year-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    New Year's Eve
                  </a>
                  <a href="https://mirelleinspo.com/blog/thanksgiving-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Thanksgiving
                  </a>
                  <a href="https://mirelleinspo.com/blog/holiday-vacation-nails-travel-guide" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Vacation Nails
                  </a>
                  <a href="https://mirelleinspo.com/blog/goddess-nails-2025" style={{color: '#2563eb', textDecoration: 'underline'}} className="text-sm hover:text-burgundy-600">
                    Goddess Nails
                  </a>
                </div>
              </div>
            </div>

            {/* Final CTA */}
            <div className="bg-gradient-to-r from-burgundy-600 to-pink-600 rounded-2xl p-8 md:p-12 text-center text-white">
              <h2 className="font-serif text-3xl md:text-4xl font-bold mb-4">
                Ready to Start Your Nail Art Journey?
              </h2>
              <p className="text-lg mb-8 text-white/90 max-w-2xl mx-auto">
                You've got everything you need. Pick one design from the Ultra Easy section and try it this week. No pressure, no judgment—just have fun creating.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://mirelleinspo.com/pinterest" className="bg-white text-burgundy-600 px-8 py-4 rounded-full font-bold hover:bg-gray-100 transition-all transform hover:scale-105 shadow-xl">
                  Follow for More Inspo
                </a>
                <a href="https://mirelleinspo.com/shop" className="glass-card-dark px-8 py-4 rounded-full font-bold hover:bg-white/20 transition-all">
                  Shop Nail Supplies
                </a>
              </div>
            </div>

          </div>
        </section>
      </div>
    </>
  );
}
