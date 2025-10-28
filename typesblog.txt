import { FAQItem, TutorialStep, TutorialMetadata, VideoMetadata } from '@/lib/generateSchemas';

// ✅ NEW: Gallery image interface
export interface GalleryImage {
  url: string;
  alt: string;
  width: number;
  height: number;
  caption?: string;
}

// ✅ NEW: Rating interface for aggregate ratings
export interface Rating {
  value: number;
  count: number;
}

export interface BlogPost {
  slug: string;
  title: string;
  excerpt: string;
  content: string;
  date: string;
  author: string;
  tags: string[];
  image?: string;
  readTime: number | string;  // CHANGED: Accept "5 min" or 5
  canonical: string;
  updatedDate?: string;
  category?: string;
  imageAlt?: string;  // ADDED
  imageWidth?: number;  // ADDED
  imageHeight?: number;  // ADDED
  dateModified?: string;  // ADDED
  wordCount?: number;  // ADDED
  faqItems?: FAQItem[];
  tutorialSteps?: TutorialStep[];
  tutorialMetadata?: TutorialMetadata;
  videoMetadata?: VideoMetadata;
  galleryImages?: GalleryImage[]; // ✅ Added: Array of gallery image URLs
    // ✨ NEW PROPERTY - Add this to your existing interface
  tldr?: {
    summary: string[];
    keyTakeaways?: string[];
  };

}

export interface BlogMetadata {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  author: string;
  tags: string[];
  image?: string;
  galleryImages?: GalleryImage[];  // ✅ NEW
  rating?: Rating;  // ✅ NEW
  readTime: number | string;  // CHANGED: Accept "5 min" or 5
  imageAlt?: string;  // ADDED
  category?: string;
}
