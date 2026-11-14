import React, { useState } from 'react';
import { Menu, X } from 'lucide-react';
import type { Lang } from '../types';

interface TopBarProps {
  lang: Lang;
}

export const TopBar: React.FC<TopBarProps> = ({ lang }) => {
  const [mobileOpen, setMobileOpen] = useState(false);

  const navLinks = [
    { href: '#journey', label: lang === 'ar' ? 'الرحلة التعليمية' : 'KG–G12 Journey' },
    { href: '#project', label: lang === 'ar' ? 'المشروع والتوسع' : 'P0–P10 & Scale' },
    { href: '#launch', label: lang === 'ar' ? 'حفل الإطلاق' : 'Launch Event' },
    { href: '#governance', label: lang === 'ar' ? 'الحوكمة والقرارات' : 'Governance' },
  ];

  const handleNavClick = () => setMobileOpen(false);

  return (
    <header className="sticky top-0 z-40 h-16 bg-[#0B1B3D]/95 backdrop-blur-sm border-b border-white/10 text-white">
      <div className="max-w-[1440px] mx-auto h-full px-4 sm:px-6 lg:px-10 flex items-center justify-between gap-8">
        <a
          href="#top"
          className="text-lg font-bold tracking-tight text-white whitespace-nowrap shrink-0 ltr-inline"
        >
          Green Grow Bot
        </a>

        <nav
          aria-label={lang === 'ar' ? 'التنقل الرئيسي' : 'Primary navigation'}
          className="hidden md:flex items-center gap-7 text-sm font-medium text-slate-200"
        >
          {navLinks.map((link) => (
            <a
              key={link.href}
              href={link.href}
              className="hover:text-[#D4AF37] transition-colors duration-150 whitespace-nowrap shrink-0 py-1 border-b border-transparent hover:border-[#D4AF37]"
            >
              {link.label}
            </a>
          ))}
        </nav>

        <div className="flex items-center gap-3 shrink-0">
          <a
            href="#governance"
            className="hidden sm:inline-flex items-center justify-center px-4 py-2 text-xs font-bold bg-[#D4AF37] text-[#0B1B3D] hover:bg-[#E2C258] transition-colors duration-150 whitespace-nowrap shrink-0 rounded"
          >
            {lang === 'ar' ? 'بوابة الاعتماد التنفيذي' : 'Executive Sign-off'}
          </a>

          <button
            type="button"
            onClick={() => setMobileOpen((prev) => !prev)}
            aria-expanded={mobileOpen}
            aria-label={lang === 'ar' ? 'فتح القائمة' : 'Toggle menu'}
            className="md:hidden inline-flex items-center justify-center w-10 h-10 text-white hover:text-[#D4AF37] rounded border border-white/15"
          >
            {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {mobileOpen && (
        <div className="md:hidden bg-[#0B1B3D] border-b border-white/15 px-4 py-4 space-y-2">
          {navLinks.map((link) => (
            <a
              key={link.href}
              href={link.href}
              onClick={handleNavClick}
              className="block py-2.5 text-sm font-medium text-slate-100 hover:text-[#D4AF37] border-b border-white/10"
            >
              {link.label}
            </a>
          ))}
          <a
            href="#governance"
            onClick={handleNavClick}
            className="block mt-3 text-center py-2.5 px-4 text-sm font-bold bg-[#D4AF37] text-[#0B1B3D] rounded"
          >
            {lang === 'ar' ? 'بوابة الاعتماد التنفيذي' : 'Executive Sign-off'}
          </a>
        </div>
      )}
    </header>
  );
};
