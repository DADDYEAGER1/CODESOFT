import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  
  // ✅ Image Optimization - LOCAL IMAGES PRIORITY + Remote fallback
  images: {
    // Local images from public folder (PRIORITY)
    localPatterns: [
      {
        pathname: '/images/shop/**',
        search: '',
      },
      {
        pathname: '/images/**',
        search: '',
      },
    ],
    
    // Modern image formats (60-70% smaller files)
    formats: ['image/avif', 'image/webp'],
    
    // Cache optimized images for 1 year
    minimumCacheTTL: 31536000,
    
    // Responsive image sizes for different devices
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    
    // Remote patterns (fallback for external images)
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'mirelleinspo.com',
      },
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
      },
      {
        protocol: 'https',
        hostname: '*.media-amazon.com',
      },
      {
        protocol: 'https',
        hostname: 'm.media-amazon.com',
      },
    ],
    
    // Don't disable optimization
    unoptimized: false,
    
    // Allow SVG with security
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },

  // ✅ Headers for SEO, Security, and Caching
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "X-Content-Type-Options",
            value: "nosniff",
          },
          {
            key: "X-Frame-Options",
            value: "SAMEORIGIN",
          },
          {
            key: "X-XSS-Protection",
            value: "1; mode=block",
          },
          {
            key: "Referrer-Policy",
            value: "strict-origin-when-cross-origin",
          },
          {
            key: "Permissions-Policy",
            value: "camera=(), microphone=(), geolocation=()",
          },
        ],
      },
      // Cache shop images aggressively
      {
        source: "/images/shop/:path*",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
      // Cache all other images
      {
        source: "/images/:path*",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
      // Cache Next.js static assets
      {
        source: "/_next/static/:path*",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
      // Cache optimized Next.js images
      {
        source: "/_next/image/:path*",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
    ];
  },

  // Enable SWR for ISR with optimized settings
  onDemandEntries: {
    maxInactiveAge: 60 * 1000,
    pagesBufferLength: 5,
  },

  // Performance optimizations
  compress: true,
  generateEtags: true,
  trailingSlash: false,
  reactStrictMode: true,

  // Experimental features
  experimental: {
    optimizePackageImports: ["lodash-es", "fuse.js"],
    optimizeCss: true,
  },

  // Webpack optimization
  webpack: (config, { isServer, dev }) => {
    if (!isServer && !dev) {
      config.optimization = {
        ...config.optimization,
        splitChunks: {
          chunks: 'all',
          cacheGroups: {
            default: false,
            vendors: false,
            vendor: {
              name: 'vendor',
              chunks: 'all',
              test: /node_modules/,
              priority: 20,
            },
            common: {
              name: 'common',
              minChunks: 2,
              chunks: 'all',
              priority: 10,
              reuseExistingChunk: true,
              enforce: true,
            },
            lib: {
              test: /[\\/]node_modules[\\/](react|react-dom|next)[\\/]/,
              name: 'lib',
              chunks: 'all',
              priority: 30,
            },
          },
        },
        minimize: true,
      };
    }

    // Handle SVGs as React components
    config.module.rules.push({
      test: /\.svg$/,
      use: ['@svgr/webpack'],
    });

    return config;
  },

  productionBrowserSourceMaps: false,

  async redirects() {
    return [];
  },
};

export default nextConfig;
