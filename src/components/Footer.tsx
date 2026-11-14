import React from 'react';
import { CANONICAL_META } from '../data/projectEventData';
import type { Lang } from '../types';

interface FooterProps {
  lang: Lang;
  onToggleLang: (next: Lang) => void;
}

export const Footer: React.FC<FooterProps> = ({ lang, onToggleLang }) => {
  return (
    <footer className="bg-[#0B1B3D] text-slate-300 border-t border-white/15 py-10">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div className="space-y-1.5">
          <div className="text-base font-bold text-white flex flex-wrap items-center gap-2">
            <span className="ltr-inline">Green Grow Bot</span>
            <span aria-hidden="true" className="text-[#D4AF37]">·</span>
            <span>{CANONICAL_META.host[lang]}</span>
          </div>
          <p className="text-xs text-slate-300">
            {CANONICAL_META.location[lang]} · {CANONICAL_META.tagline[lang]} ·{' '}
            <span className="ltr-inline text-[#E2C258]">{CANONICAL_META.hashtag}</span>
          </p>
          <p className="text-[11px] text-slate-400">
            {lang === 'ar'
              ? 'جميع البيانات والأرقام التقديرية مستندة إلى المواصفة المرجعية المعتمدة داخلياً (نسخة 1.0 — تحديث 10 نوفمبر 2026).'
              : 'All figures and provisional benchmarks trace strictly to the internal Canonical Spec (v1.0 — Nov 10, 2026 baseline reset).'}
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-4 text-xs">
          <a href="#journey" className="hover:text-white transition-colors">
            {lang === 'ar' ? 'الرحلة التعليمية' : 'KG–G12'}
          </a>
          <a href="#project" className="hover:text-white transition-colors">
            {lang === 'ar' ? 'المشروع والتوسع' : 'P0–P10'}
          </a>
          <a href="#launch" className="hover:text-white transition-colors">
            {lang === 'ar' ? 'حفل الإطلاق' : 'Launch Event'}
          </a>
          <a href="#governance" className="hover:text-white transition-colors">
            {lang === 'ar' ? 'الحوكمة' : 'Governance'}
          </a>
          <button
            type="button"
            onClick={() => onToggleLang(lang === 'ar' ? 'en' : 'ar')}
            className="px-3 py-1.5 border border-white/25 rounded text-white hover:border-[#D4AF37] hover:text-[#D4AF37] transition-colors whitespace-nowrap shrink-0"
          >
            {lang === 'ar' ? 'English View' : 'النسخة العربية'}
          </button>
        </div>
      </div>
    </footer>
  );
};
