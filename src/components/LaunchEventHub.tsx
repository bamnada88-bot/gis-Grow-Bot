import React, { useState } from 'react';
import {
  AlertCircle,
  Calendar,
  Check,
  Clock,
  Copy,
  MapPin,
  Mic,
  Shield,
} from 'lucide-react';
import {
  CANONICAL_META,
  DEMO_BEATS,
  EVENT_SCHEDULE,
  GO_NOGO_GATES,
  ROLE_BADGES,
} from '../data/projectEventData';
import type { Lang } from '../types';

interface LaunchEventHubProps {
  lang: Lang;
}

export const LaunchEventHub: React.FC<LaunchEventHubProps> = ({ lang }) => {
  const [filter, setFilter] = useState<'all' | 'plenary' | 'gate' | 'reception' | 'setup'>('all');
  const [copiedId, setCopiedId] = useState<'invite' | 'press' | null>(null);

  const visibleSchedule =
    filter === 'all'
      ? EVENT_SCHEDULE
      : EVENT_SCHEDULE.filter((item) => item.category === filter);

  const officialInviteText =
    lang === 'ar'
      ? `دعوة رسمية لحضور حفل إطلاق مبادرة Green Grow Bot\n«${CANONICAL_META.tagline.ar}»\n\nتتشرف مدارس جرين إنترناشونال (Green International Schools — العبور الجديدة) بدعوة سيادتكم لحضور حفل إطلاق مبادرة تعليمية تطبيقية تربط موضوعات مختارة من المناهج بالممارسة العملية.\n\nالداعي: ${CANONICAL_META.founder.ar} ${CANONICAL_META.founderTitleStatus.ar}\nالتاريخ: ${CANONICAL_META.eventDate.ar}\nالمكان المقترح: ${CANONICAL_META.venueName} ${CANONICAL_META.venueBookingStatus.ar}\nالبرنامج: التسجيل 18:00 · الافتتاح 18:30 (85 دقيقة) · الاستقبال 20:15\n\nملاحظة بروتوكولية: بيانات تأكيد الحضور النهائية (RSVP) وشعار AXMIND يُضافان فقط بعد الاعتماد المكتوب.`
      : `Official Invitation: Green Grow Bot Launch Event\n"${CANONICAL_META.tagline.en}"\n\nGreen International Schools (Al Obour New City) invites you to the official launch of an applied robotics initiative connecting classroom curricula with hands-on building.\n\nHost / Lead: ${CANONICAL_META.founder.en} ${CANONICAL_META.founderTitleStatus.en}\nDate: ${CANONICAL_META.eventDate.en}\nProposed Venue: ${CANONICAL_META.venueName} ${CANONICAL_META.venueBookingStatus.en}\nSchedule: Registration 18:00 · Plenary 18:30 (85 min) · Reception 20:15\n\nProtocol Note: Final RSVP desk details & AXMIND branding applied only after written approval.`;

  const pressBriefText =
    lang === 'ar'
      ? `بيان تعريفي أولي — مبادرة Green Grow Bot\nالجهة المستضيفة: ${CANONICAL_META.host.ar}، ${CANONICAL_META.location.ar}\nالشعار المعتمد: «${CANONICAL_META.tagline.ar}»\n\nتقوم المبادرة على بناء الطالب لمشروع تطبيقي واحد يتطور معه عبر 9 مراحل من KG1 إلى Grade 12 مع بقاء المنهج الأكاديمي أساساً، وبدء التجربة الاستهلالية الموصى بها من الصف السادس (G6). تُقاس المخرجات وفق إطار كيركباتريك الأربعة وبموافقات كتابية مسبقة لأي تصوير طلابي، ودون تقديم أي ضمانات لوظيفة أو قبول جامعي.`
      : `Press Backgrounder — Green Grow Bot Initiative\nHost: ${CANONICAL_META.host.en}, ${CANONICAL_META.location.en}\nTagline: "${CANONICAL_META.tagline.en}"\n\nStudents build one cumulative robotics project across 9 stages (KG1–G12) enriching core subjects, with Grade 6 recommended as initial pilot entry. Outcomes are measured via Kirkpatrick L1–L4 under strict written parental media consent and zero job/admission guarantees.`;

  const handleCopy = async (type: 'invite' | 'press', text: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedId(type);
      setTimeout(() => setCopiedId(null), 2200);
    } catch {
      setCopiedId(null);
    }
  };

  return (
    <section id="launch" className="py-16 lg:py-20 bg-[#FBF9F4] text-[#0B0F14] border-b border-[#E5E7EB]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 space-y-10">
        {/* Section Header */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-[#0B1B3D]/15">
          <div className="space-y-2 max-w-3xl">
            <div className="text-xs font-bold text-[#2D78FF]">
              {lang === 'ar'
                ? '03. مركز تشغيل حفل الإطلاق والبروتوكول (الأحد 15 نوفمبر 2026)'
                : '03. Launch Event Runbook & Protocol Studio (Sunday, 15 Nov 2026)'}
            </div>
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#0B1B3D]">
              {lang === 'ar'
                ? 'مؤتمر مصغّر + عرض حيّ + استقبال (85 دقيقة منضبطة)'
                : 'Mini-Conference + Live Demo + Reception (85-Minute Plenary)'}
            </h2>
            <div className="flex flex-wrap items-center gap-3 text-xs sm:text-sm text-slate-600">
              <span className="inline-flex items-center gap-1.5">
                <Calendar className="w-4 h-4 text-[#D4AF37]" aria-hidden="true" />
                {CANONICAL_META.eventDate[lang]}
              </span>
              <span aria-hidden="true">·</span>
              <span className="inline-flex items-center gap-1.5">
                <MapPin className="w-4 h-4 text-[#D4AF37]" aria-hidden="true" />
                <span className="ltr-inline">{CANONICAL_META.venueName}</span>
                <span>{CANONICAL_META.venueBookingStatus[lang]}</span>
              </span>
            </div>
          </div>

          <div className="inline-flex flex-wrap items-center gap-1 p-1 bg-white border border-slate-200 rounded shrink-0">
            {(
              [
                { id: 'all', ar: 'الكل (14:00–21:30)', en: 'All (14:00–21:30)' },
                { id: 'plenary', ar: 'البرنامج الرئيسي (85 د)', en: '85-Min Plenary' },
                { id: 'gate', ar: 'بوابات الفحص', en: 'Go/No-Go Gates' },
                { id: 'reception', ar: 'الإعلام والاستقبال', en: 'Media & Reception' },
                { id: 'setup', ar: 'التجهيز والتفكيك', en: 'Setup & Teardown' },
              ] as const
            ).map((btn) => (
              <button
                key={btn.id}
                type="button"
                onClick={() => setFilter(btn.id)}
                className={`px-3 py-1.5 text-xs font-medium rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                  filter === btn.id
                    ? 'bg-[#0B1B3D] text-white font-bold'
                    : 'text-slate-700 hover:bg-slate-100'
                }`}
              >
                {lang === 'ar' ? btn.ar : btn.en}
              </button>
            ))}
          </div>
        </div>

        {/* Runbook Schedule Table + Live Demo Beat Sheet */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-7 bg-white border border-slate-200 rounded overflow-hidden">
            <div className="px-5 py-4 bg-[#0B1B3D] text-white flex items-center justify-between">
              <div className="flex items-center gap-2 text-sm font-bold">
                <Clock className="w-4 h-4 text-[#D4AF37]" aria-hidden="true" />
                <span>
                  {lang === 'ar' ? 'الجدول الزمني المرجعي ليوم الحفل' : 'Master Event Day Timeline'}
                </span>
              </div>
              <span className="text-xs text-slate-300 tabular-nums">
                {lang === 'ar' ? `${visibleSchedule.length} فقرات` : `${visibleSchedule.length} items`}
              </span>
            </div>

            <div className="divide-y divide-slate-200">
              {visibleSchedule.map((row, idx) => (
                <div
                  key={`${row.time}-${idx}`}
                  className="p-4 hover:bg-[#FBF9F4] transition-colors grid grid-cols-1 sm:grid-cols-12 gap-3 items-start text-xs sm:text-sm"
                >
                  <div className="sm:col-span-2 font-mono tabular-nums">
                    <div className="font-bold text-[#0B1B3D]">{row.time}</div>
                    <div className="text-[11px] text-slate-500">{row.duration[lang]}</div>
                  </div>
                  <div className="sm:col-span-6 space-y-1">
                    <div className="font-bold text-[#0B0F14]">{row.segment[lang]}</div>
                    <div className="text-xs text-slate-600">{row.goal[lang]}</div>
                  </div>
                  <div className="sm:col-span-4 sm:text-end space-y-1">
                    <div className="font-mono text-xs font-bold text-[#2D78FF]">{row.owner}</div>
                    <div className="text-[11px] text-slate-500">{row.output[lang]}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* 12-Minute Live Demo Beat Sheet + Fallback Rule */}
          <div className="lg:col-span-5 space-y-6">
            <div className="bg-white border border-slate-200 rounded p-6 space-y-5">
              <div className="flex items-center justify-between pb-3 border-b border-slate-200">
                <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
                  <Mic className="w-4 h-4 text-[#2D78FF]" aria-hidden="true" />
                  <span>
                    {lang === 'ar'
                      ? 'بطاقة إيقاع العرض الحيّ (19:00 · 12 دقيقة)'
                      : '12-Min Live Demo Beat Sheet (19:00)'}
                  </span>
                </div>
                <span className="text-xs font-mono text-slate-500">DEMO + CT</span>
              </div>

              <div className="space-y-3">
                {DEMO_BEATS.map((beat) => (
                  <div key={beat.window} className="p-3.5 bg-[#FBF9F4] border border-slate-200 rounded space-y-1">
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-[#0B1B3D]">{beat.title[lang]}</span>
                      <span className="font-mono tabular-nums text-[#2D78FF] font-semibold ltr-inline">
                        {beat.window}
                      </span>
                    </div>
                    <p className="text-xs text-slate-600">{beat.action[lang]}</p>
                    <p className="text-xs font-medium text-[#0B1B3D] pt-1">
                      {beat.spokenCue[lang]}
                    </p>
                  </div>
                ))}
              </div>

              <div className="p-4 bg-amber-50 border border-amber-200 rounded space-y-1.5">
                <div className="flex items-center gap-1.5 text-xs font-bold text-amber-900">
                  <AlertCircle className="w-4 h-4 shrink-0" aria-hidden="true" />
                  <span>
                    {lang === 'ar'
                      ? 'بروتوكول التعطل الفوري وعبارة المشغّل المعتمدة:'
                      : 'Instant Stage Contingency & Approved Cue:'}
                  </span>
                </div>
                <p className="text-xs text-amber-950 leading-relaxed">
                  {lang === 'ar'
                    ? 'إذا توقف الروبوت أو فشل الاختبار: يُفعَّل الروبوت الاحتياطي أو فيديو الـ 90 ثانية المسجّل، وتُقال العبارة المعتمدة دون اعتذار مرتبك: «شكرًا لصبركم — لدينا نسخة جاهزة، ولنتابع.»'
                    : 'If unit stalls: deploy charged backup or 90s recorded clip calmly: "Thank you for your patience — we have a ready backup unit, let us continue."'}
                </p>
              </div>
            </div>

            {/* Venue Cheops Specs & Accessibility */}
            <div className="bg-white border border-slate-200 rounded p-6 space-y-3">
              <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
                <Shield className="w-4 h-4 text-[#059669]" aria-hidden="true" />
                <span>
                  {lang === 'ar'
                    ? 'مواصفات القاعة المقترحة والإتاحة (Cheops 352 م²)'
                    : 'Proposed Hall & Accessibility Specs (Cheops 352 m²)'}
                </span>
              </div>
              <div className="text-xs text-slate-700 space-y-1.5 leading-relaxed">
                <p>
                  {lang === 'ar'
                    ? 'السعة المرجعية (مصدر الفندق، غير مؤكد كحجز): مسرحي 396 | بانكيت 240 | استقبال 240 + Pre-function I/II للتسجيل والضيافة.'
                    : 'Hotel published capacity (unconfirmed booking): Theater 396 | Banquet 240 | Reception 240 + Pre-function I/II.'}
                </p>
                <p>
                  {lang === 'ar'
                    ? 'الإتاحة والسلامة: مسار كراسٍ متحركة دون درج للمسرح ومنطقة العرض، حواجز 60 سم وشريط عزل 1 م، وبديل فوري لقاعات داخلية بمدارس جرين إنترناشونال عند تعذر التأكيد الكتابي.'
                    : 'Accessibility & Safety: Step-free wheelchair access, 60cm barriers + 1m floor buffer, and instant fallback to internal GIS hall if hotel booking remains unconfirmed.'}
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* 6 Go/No-Go Gates + 10 Roles */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          <div className="lg:col-span-7 bg-white border border-slate-200 rounded p-6 space-y-4">
            <h3 className="text-lg font-bold text-[#0B1B3D]">
              {lang === 'ar' ? 'بوابات القرار الميدانية الست (Go / No-Go)' : 'Six On-Site Go / No-Go Gates'}
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {GO_NOGO_GATES.map((gate) => (
                <div key={gate.id} className="p-3.5 bg-[#FBF9F4] border border-slate-200 rounded space-y-1.5 text-xs">
                  <div className="flex items-center justify-between font-mono">
                    <span className="font-bold text-[#0B1B3D]">
                      {lang === 'ar' ? `بوابة ${gate.id}` : `Gate ${gate.id}`} · {gate.time}
                    </span>
                    <span className="text-[#2D78FF] font-bold">{gate.owner}</span>
                  </div>
                  <div className="font-bold text-sm text-[#0B1B3D]">{gate.title[lang]}</div>
                  <div className="text-slate-600">{gate.criteria[lang]}</div>
                  <div className="pt-1 border-t border-slate-200 text-amber-800">
                    {lang === 'ar' ? 'البديل: ' : 'Fallback: '}
                    {gate.fallback[lang]}
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="lg:col-span-5 bg-white border border-slate-200 rounded p-6 space-y-4">
            <h3 className="text-lg font-bold text-[#0B1B3D]">
              {lang === 'ar' ? 'هيكل الأدوار العشر (بانتظار تسمية الأفراد)' : '10 Canonical Event Roles (Open Assignments)'}
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
              {ROLE_BADGES.map((role) => (
                <div
                  key={role.code}
                  className="p-3 bg-[#FBF9F4] border border-slate-200 rounded flex items-center justify-between gap-2"
                >
                  <span className="font-medium text-[#0B0F14]">{role[lang]}</span>
                  <span className="font-mono font-bold text-[#0B1B3D] shrink-0">{role.code}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Invitation & Press Copy Studio */}
        <div className="bg-[#0B1B3D] text-white rounded p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-4">
            <div className="flex items-center justify-between gap-4">
              <div>
                <div className="text-xs font-bold text-[#D4AF37]">
                  {lang === 'ar' ? 'استوديو الدعوة الرسمية' : 'Official Invitation Copy'}
                </div>
                <h3 className="text-lg font-bold mt-0.5">
                  {lang === 'ar' ? 'نص الدعوة المعتمد (منضبط الشعار والحجز)' : 'Compliant Invitation Draft'}
                </h3>
              </div>
              <button
                type="button"
                onClick={() => handleCopy('invite', officialInviteText)}
                className="inline-flex items-center gap-1.5 px-3 py-2 text-xs font-bold bg-[#D4AF37] text-[#0B1B3D] rounded hover:bg-[#E2C258] transition-colors shrink-0"
              >
                {copiedId === 'invite' ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                <span>
                  {copiedId === 'invite'
                    ? lang === 'ar'
                      ? 'تم النسخ'
                      : 'Copied'
                    : lang === 'ar'
                    ? 'نسخ النص'
                    : 'Copy Text'}
                </span>
              </button>
            </div>
            <pre className="whitespace-pre-wrap font-sans text-xs sm:text-sm bg-white/6 border border-white/15 rounded p-4 text-slate-100 leading-relaxed">
              {officialInviteText}
            </pre>
          </div>

          <div className="space-y-4">
            <div className="flex items-center justify-between gap-4">
              <div>
                <div className="text-xs font-bold text-[#D4AF37]">
                  {lang === 'ar' ? 'الملف الصحفي والإعلامي' : 'Press Backgrounder Copy'}
                </div>
                <h3 className="text-lg font-bold mt-0.5">
                  {lang === 'ar' ? 'الإحاطة الإعلامية المعتمدة' : 'Approved Media Summary'}
                </h3>
              </div>
              <button
                type="button"
                onClick={() => handleCopy('press', pressBriefText)}
                className="inline-flex items-center gap-1.5 px-3 py-2 text-xs font-bold bg-white text-[#0B1B3D] rounded hover:bg-slate-100 transition-colors shrink-0"
              >
                {copiedId === 'press' ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                <span>
                  {copiedId === 'press'
                    ? lang === 'ar'
                      ? 'تم النسخ'
                      : 'Copied'
                    : lang === 'ar'
                    ? 'نسخ البيان'
                    : 'Copy Brief'}
                </span>
              </button>
            </div>
            <pre className="whitespace-pre-wrap font-sans text-xs sm:text-sm bg-white/6 border border-white/15 rounded p-4 text-slate-100 leading-relaxed">
              {pressBriefText}
            </pre>
            <p className="text-xs text-slate-300">
              {CANONICAL_META.axmindRule[lang]}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};
