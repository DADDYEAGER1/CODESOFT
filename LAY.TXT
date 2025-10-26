import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Script from "next/script";
import { Inter, Cormorant_Garamond } from 'next/font/google';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

const cormorant = Cormorant_Garamond({
  weight: ['400', '600', '700'],
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-cormorant',
});
export const metadata: Metadata = {
  metadataBase: new URL('https://mirelleinspo.com'),
  title: {
    default: "Mirellé Inspo | Nail Art Ideas, Trends & Tutorials 2025",
    template: "%s | Mirellé Inspo"
  },
  description: "Explore 2025's top nail art trends, DIY tutorials, seasonal nail designs, and expert tips. Get inspired for Pinterest-worthy nails every mood and occasion.",
  keywords: [
    "nail art ideas 2025",
    "nail trends 2025",
    "DIY nail tutorials",
    "seasonal nail designs",
    "Pinterest nails",
    "modern nail inspiration",
    "nail care tips",
    "winter nails 2025",
    "Christmas nails",
    "acrylic nails",
    "gel nail designs",
    "nail art for beginners",
    "salon nail ideas",
    "at-home manicure"
  ],
  authors: [{ name: "Avery chen", url: "https://mirelleinspo.com/about" }],
  creator: "Avery chen",
  publisher: "Mirellé Inspo",
  formatDetection: {
    telephone: false,
    email: false,
    address: false,
  },
  
  // Global geo-targeting (won't hurt international reach)
  other: {
    'distribution': 'global',
    'rating': 'general',
    'coverage': 'worldwide',
    'target': 'all',
    'audience': 'all',
    'language': 'en-US',
    'classification': 'Beauty, Fashion, Nail Art, Tutorials, DIY, Lifestyle',
    'referrer': 'always',
    'revisit-after': '7 days',
  },

  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://mirelleinspo.com",
    siteName: "Mirellé Inspo",
    title: "Mirellé Inspo | Nail Art Ideas, Trends & Tutorials 2025",
    description: "Discover the latest nail art trends, creative tutorials, seasonal designs, and Pinterest-inspired nail ideas curated by Mirelle.",
    images: [
      {
        url: "/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Mirellé Inspo - Nail Art Inspiration",
      },
    ],
  },
  
  twitter: {
    card: "summary_large_image",
    title: "Mirellé Inspo | Nail Art Ideas & Tutorials 2025",
    description: "Stay ahead with 2025 nail trends, seasonal designs, and Pinterest-worthy tutorials. Expert tips and inspiration for every mood.",
    images: ["/twitter-image.jpg"],
    creator: "@mirelleinspo",
    site: "@mirelleinspo",
  },
  
  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  
icons: {
  icon: [
    { url: "/favicon.ico", sizes: "any" },
    { url: "/favicon-96x96.png", sizes: "96x96", type: "image/png" },
    { url: "/favicon.svg", type: "image/svg+xml" },
  ],
  shortcut: "/favicon.ico",
  apple: [
    { url: "/apple-touch-icon.png", sizes: "180x180", type: "image/png" },
  ],
},
manifest: "/site.webmanifest",

  
  alternates: {
    canonical: "https://mirelleinspo.com",
    // Multi-region language support for global reach
    languages: {
      'en-US': 'https://mirelleinspo.com',
      'en-GB': 'https://mirelleinspo.com',
      'en-CA': 'https://mirelleinspo.com',
      'en-AU': 'https://mirelleinspo.com',
      'en': 'https://mirelleinspo.com',
    },
  },
  
verification: {
  google: 'YOUR_GOOGLE_VERIFICATION_CODE', // Get from Google Search Console
  other: {
    'msvalidate.01': 'YOUR_BING_VERIFICATION_CODE',
  },
},

  
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // Enhanced structured data for AI bots
  const organizationSchema = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://mirelleinspo.com/#organization",
    "name": "Mirellé",
    "alternateName": "Mirelle",
    "url": "https://mirelleinspo.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://mirelleinspo.com/apple-touch-icon.png",
      "width": 512,
      "height": 512
    },
    "description": "Expert nail art inspiration, tutorials, and seasonal beauty trends for modern women",
    "sameAs": [
      "https://www.pinterest.com/mirelle_inspo",
      "https://www.instagram.com/mirelle_inspo",
      "https://www.wikidata.org/wiki/mirelle_inspo",
      "https://x.com/mirelleinspo",
    ],
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "Customer Service",
      "url": "https://mirelleinspo.com/contact"
    },
    // Global audience targeting
    "areaServed": {
      "@type": "Place",
      "name": "Worldwide"
    },
    "audience": {
      "@type": "Audience",
      "audienceType": "Global",
      "geographicArea": {
        "@type": "Place",
        "name": "Worldwide"
      }
    }
  };

  const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": "https://mirelleinspo.com/#website",
    "name": "Mirellé",
    "url": "https://mirelleinspo.com",
    "description": "Nail art ideas, trends, tutorials, and inspiration for 2025. Professional tips for beautiful, healthy nails.",
    "publisher": {
      "@type": "Organization",
      "@id": "https://mirelleinspo.com/#organization",
      "name": "Mirellé Inspo",
    },
    "inLanguage": "en-US",
    "potentialAction": {
      "@type": "SearchAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": "https://mirelleinspo.com/search?q={search_term_string}"
      },
      "query-input": "required name=search_term_string"
    }
  };

  // BreadcrumbList for better content structure
  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://mirelleinspo.com"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Blog",
        "item": "https://mirelleinspo.com/blog"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Topics",
        "item": "https://mirelleinspo.com/topics"
      }
    ]
  };

  return (
    <html lang="en-US">
      <head>
        {/* Global geo-targeting meta tags (won't hurt international reach) */}
        <meta name="distribution" content="global" />
        <meta name="coverage" content="worldwide" />
        <meta name="target" content="all" />
        <meta name="audience" content="all" />
        <meta httpEquiv="content-language" content="en-US" />
        <meta name="language" content="English" />
        <meta name="rating" content="general" />
        <meta name="revisit-after" content="7 days" />
        
        {/* AI Bot friendly meta tags */}
        <meta name="referrer" content="always" />
        <meta name="classification" content="Beauty, Fashion, Nail Art, Tutorials, DIY, Lifestyle" />
        

        {/* ✅ KEEP THESE */}
        <link rel="preconnect" href="https://pagead2.googlesyndication.com" />
        <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
        
        {/* Fonts with display=swap for better performance */}
        <link
          href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap"
          rel="stylesheet"
        />

        {/* AdSense verification meta tag */}
        <meta name="google-adsense-account" content="ca-pub-1145734682794444" />
        
        {/* Pinterest Save Button Script */}
        {/* <script async defer src="//assets.pinterest.com/js/pinit.js"></script> */}
      </head>

      <body className="antialiased">
        {/* Google Tag Manager (noscript) */}
        <noscript>
          <iframe
            src="https://www.googletagmanager.com/ns.html?id=GTM-WPW9XBW8"
            height="0"
            width="0"
            style={{ display: "none", visibility: "hidden" }}
            title="Google Tag Manager"
          ></iframe>
        </noscript>

        {/* GA4 Analytics */}
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-4BZ9QKQZ73"
          strategy="afterInteractive"
        />
        <Script id="ga4-init" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-4BZ9QKQZ73', {
              page_path: window.location.pathname,
              send_page_view: true
            });
          `}
        </Script>
        {/* <meta name="msvalidate.01" content="YOUR_BING_CODE_HERE" /> */}

        {/* Google AdSense */}
        <Script
          id="adsense-script"
          strategy="afterInteractive"
          async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1145734682794444"
          crossOrigin="anonymous"
        />
        <script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
    __html: JSON.stringify(breadcrumbSchema),
  }}
/>
        {/* Preload critical font */}
<link
  rel="preload"
  href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap"
  as="style"
/>

{/* Canonical tag */}
<link rel="canonical" href="https://mirelleinspo.com" />

{/* Mobile web app meta */}
<meta name="mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />

{/* Theme color */}
<meta name="theme-color" content="#000000" />
        
        {/* ADD WEB VITALS TRACKING HERE - AFTER ADSENSE */}
        <Script id="web-vitals" strategy="afterInteractive">
          {`
            (function() {
              function sendToAnalytics(metric) {
                if (window.gtag) {
                  window.gtag('event', metric.name, {
                    value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
                    event_category: 'Web Vitals',
                    event_label: metric.id,
                    non_interaction: true,
                  });
                }
              }
              
              if ('PerformanceObserver' in window) {
                // Track Largest Contentful Paint (LCP)
                try {
                  const lcpObserver = new PerformanceObserver((list) => {
                    const entries = list.getEntries();
                    const lastEntry = entries[entries.length - 1];
                    sendToAnalytics({
                      name: 'LCP',
                      value: lastEntry.renderTime || lastEntry.loadTime,
                      id: 'v1-' + Date.now()
                    });
                  });
                  lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
                } catch (e) {}
                
                // Track First Input Delay (FID)
                try {
                  const fidObserver = new PerformanceObserver((list) => {
                    const entries = list.getEntries();
                    entries.forEach((entry) => {
                      sendToAnalytics({
                        name: 'FID',
                        value: entry.processingStart - entry.startTime,
                        id: 'v1-' + Date.now()
                      });
                    });
                  });
                  fidObserver.observe({ entryTypes: ['first-input'] });
                } catch (e) {}
                
                // Track Cumulative Layout Shift (CLS)
                try {
                  let clsValue = 0;
                  const clsObserver = new PerformanceObserver((list) => {
                    list.getEntries().forEach((entry) => {
                      if (!entry.hadRecentInput) {
                        clsValue += entry.value;
                      }
                    });
                  });
                  clsObserver.observe({ entryTypes: ['layout-shift'] });
                  
                  // Send CLS on page hide
                  addEventListener('visibilitychange', () => {
                    if (document.visibilityState === 'hidden') {
                      sendToAnalytics({
                        name: 'CLS',
                        value: clsValue,
                        id: 'v1-' + Date.now()
                      });
                    }
                  });
                } catch (e) {}
              }
            })();
          `}
        </Script>

        {/* Enhanced Structured Data for AI Understanding */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(organizationSchema),
          }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(websiteSchema),
          }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(breadcrumbSchema),
          }}
        />

        <Header />
        <main className="min-h-screen" id="main-content" role="main">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
