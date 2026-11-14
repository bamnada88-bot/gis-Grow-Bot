import React, { useState } from 'react';
import { ArrowDownLeft, ArrowDownRight, CheckSquare, Globe, ShieldAlert } from 'lucide-react';
import { CANONICAL_META } from '../data/projectEventData';
import type { AudienceLens, Lang } from '../types';

interface HeroSectionProps {
  lang: Lang;
  onToggleLang: (next: Lang) => void;
  lens: AudienceLens;
  onChangeLens: (next: AudienceLens) => void;
}

export const HeroSection: React.FC<HeroSectionProps> = ({
  lang,
  onToggleLang,
  lens,
  onChangeLens,
}) => {
  const [activeVisual, setActiveVisual] = useState<'infographic' | 'invitation' | 'presskit'>('infographic');
  const [imgError, setImgError] = useState<Record<string, boolean>>({});

  const lensSummary: Record<AudienceLens, { title: string; body: string }> = {
    executive: {
      title: lang === 'ar' ? 'منظور القيادة التنفيذية وإدارة المشروع' : 'Executive Leadership & PM Lens',
      body:
        lang === 'ar'
          ? 'تركّز المراجعة الحالية على إغلاق خط الأساس الحرج (متبقي 5 أيام على 15 نوفمبر 2026 وفق تحديث 10 نوفمبر)، واعتماد سيناريو الميزانية A (164,268 – 191,418 ج.م تقديراً)، وحسم القرارات الـ 13 المعلّقة قبل أي صرف أو نشر.'
          : 'Priority focus on the Nov 10 baseline reset (5 days to 15 Nov 2026), adopting Scenario A (164,268–191,418 EGP estimate), and closing the 13 pending executive approvals prior to spend or dispatch.',
    },
    parent: {
      title: lang === 'ar' ? 'منظور أولياء الأمور والأسرة' : 'Parents & Families Lens',
      body:
        lang === 'ar'
          ? 'يبني ابنكم وبنتكم مشروعاً تطبيقياً واحداً يتطور معهم من KG1 إلى Grade 12 دون المساس بالمناهج الأساسية، وبضوابط سلامة صارمة (لا لحام قبل الصف التاسع، ولا تصوير أو بيانات طالب دون موافقة ولي الأمر الكتابية).'
          : 'Your child builds one cumulative applied project from KG1 through Grade 12 enriching core academics—under strict safety rules (zero soldering before G9, mandatory written parental consent for any media).',
    },
    partner: {
      title: lang === 'ar' ? 'منظور الشركاء والجهات الرسمية والأكاديمية' : 'Institutional & Academic Partners Lens',
      body:
        lang === 'ar'
          ? 'نموذج قابل للقياس وفق إطار كيركباتريك (L1–L4) بثلاث صيغ تشغيلية تشمل نسخة منخفضة التكلفة للمدارس العامة ومراكز الشباب، ومراجعة قانونية موثقة، دون أي شعارات أو ادعاءات غير معتمدة.'
          : 'A measurable Kirkpatrick L1–L4 educational framework with 3 delivery formats including a low-cost public school model, formal legal compliance, and zero unapproved endorsements.',
    },
  };

  const visualAssets = {
    infographic: {
      src: './assets/aistudio/Green_Grow_Bot_Visual_Reference_2f0e73c8.jpeg',
      label: lang === 'ar' ? 'مسار KG–G12' : 'KG–G12 Map',
      caption:
        lang === 'ar'
          ? 'المرجع البصري لمراحل تطور الروبوت الواحد مع الطالب من الروضة إلى الصف الثاني عشر.'
          : 'Visual reference showing one cumulative robotics architecture evolving from KG to Grade 12.',
    },
    invitation: {
      src: './assets/aistudio/Green_Grow_Bot_Invitation_Digital_933b835e.png',
      label: lang === 'ar' ? 'الدعوة الرسمية' : 'Invitation',
      caption:
        lang === 'ar'
          ? 'بطاقة الدعوة الرقمية لحفل الإطلاق — الأحد 15 نوفمبر 2026 (بيانات الحجز والاعتماد قيد الاستكمال).'
          : 'Official digital launch invitation for Sunday, 15 Nov 2026 (venue booking & contact confirmation pending).',
    },
    presskit: {
      src: './assets/aistudio/presskit_____pk_p1_5ca59078.png',
      label: lang === 'ar' ? 'حقيبة الصحفيين' : 'Press Kit',
      caption:
        lang === 'ar'
          ? 'غلاف الحقيبة الصحفية المعتمدة من مدارس جرين إنترناشونال — العبور الجديدة.'
          : 'Official Press Kit cover prepared for Green International Schools, Al Obour New City.',
    },
  };

  const currentAsset = visualAssets[activeVisual];
  const ArrowIcon = lang === 'ar' ? ArrowDownLeft : ArrowDownRight;

  return (
    <section id="top" className="bg-[#0B1B3D] text-white border-b border-[#D4AF37]/30">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 pt-5 pb-12 lg:pb-14">
        {/* Workspace Control Toolbar (placed inside Hero, preserving clean 3-zone header) */}
        <div className="flex flex-wrap items-center justify-between gap-4 pb-6 mb-8 border-b border-white/15">
          <div className="flex flex-wrap items-center gap-2">
            <span className="text-xs font-medium text-slate-300 me-1">
              {lang === 'ar' ? 'عدسة العرض:' : 'Audience Lens:'}
            </span>
            <div className="inline-flex items-center p-1 bg-white/10 rounded border border-white/10">
              {(
                [
                  { id: 'executive', ar: 'القيادة التنفيذية', en: 'Executive' },
                  { id: 'parent', ar: 'أولياء الأمور', en: 'Parents' },
                  { id: 'partner', ar: 'الشركاء والجهات', en: 'Partners' },
                ] as const
              ).map((opt) => (
                <button
                  key={opt.id}
                  type="button"
                  onClick={() => onChangeLens(opt.id)}
                  className={`px-3 py-1.5 text-xs font-medium rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                    lens === opt.id
                      ? 'bg-[#D4AF37] text-[#0B1B3D] font-bold'
                      : 'text-slate-200 hover:text-white'
                  }`}
                >
                  {lang === 'ar' ? opt.ar : opt.en}
                </button>
              ))}
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="inline-flex items-center p-1 bg-white/10 rounded border border-white/10">
              <Globe className="w-3.5 h-3.5 text-[#D4AF37] mx-2 shrink-0" aria-hidden="true" />
              <button
                type="button"
                onClick={() => onToggleLang('ar')}
                className={`px-3 py-1.5 text-xs font-medium rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                  lang === 'ar' ? 'bg-white text-[#0B1B3D] font-bold' : 'text-slate-200 hover:text-white'
                }`}
              >
                العربية
              </button>
              <button
                type="button"
                onClick={() => onToggleLang('en')}
                className={`px-3 py-1.5 text-xs font-medium rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                  lang === 'en' ? 'bg-white text-[#0B1B3D] font-bold' : 'text-slate-200 hover:text-white'
                }`}
              >
                English
              </button>
            </div>
          </div>
        </div>

        {/* Balanced 2-Column Hero Split */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-stretch">
          <div className="lg:col-span-7 flex flex-col justify-between space-y-6">
            <div className="space-y-5">
              {/* Quiet Unboxed Metadata (Zero-Pill Rule) */}
              <div className="flex flex-wrap items-center gap-2 text-xs sm:text-sm text-[#E2C258] font-medium">
                <span>{CANONICAL_META.host[lang]}</span>
                <span aria-hidden="true">·</span>
                <span>{CANONICAL_META.location[lang]}</span>
                <span aria-hidden="true">·</span>
                <span>{CANONICAL_META.eventDate[lang]}</span>
              </div>

              <h1 className="text-3xl sm:text-4xl lg:text-[2.85rem] font-bold leading-[1.2] tracking-tight text-white max-w-2xl">
                {CANONICAL_META.tagline[lang]}
              </h1>

              <p className="text-base sm:text-lg text-slate-200 leading-relaxed max-w-2xl">
                {CANONICAL_META.institutionalMission[lang]}
              </p>

              {/* Dynamic Audience Lens Brief */}
              <div className="bg-white/6 border border-white/15 rounded p-5 space-y-2">
                <div className="text-xs font-bold text-[#D4AF37]">
                  {lensSummary[lens].title}
                </div>
                <p className="text-sm text-slate-100 leading-relaxed">
                  {lensSummary[lens].body}
                </p>
              </div>

              {/* Explicit Transparency Notice */}
              <div className="bg-[#132957] border border-[#D4AF37]/40 rounded p-4 flex items-start gap-3">
                <ShieldAlert className="w-5 h-5 text-[#D4AF37] shrink-0 mt-0.5" aria-hidden="true" />
                <div className="text-xs sm:text-sm text-slate-100 space-y-1">
                  <div className="font-bold text-white">
                    {lang === 'ar'
                      ? 'تنويه الشفافية وتحديث 10 نوفمبر 2026 (تبقّى 5 أيام)'
                      : 'Transparency Notice & Nov 10 Baseline Reset (5 Days Remaining)'}
                  </div>
                  <p className="text-slate-200 leading-relaxed">
                    {lang === 'ar'
                      ? `المتحدث الرئيسي: ${CANONICAL_META.founder.ar} (${CANONICAL_META.founderTitleStatus.ar}) · المكان المقترح: ${CANONICAL_META.venueName} ${CANONICAL_META.venueBookingStatus.ar} · لا يُصرف أي مبلغ على بند غير مسعّر دون RFQ.`
                      : `Lead Speaker: ${CANONICAL_META.founder.en} (${CANONICAL_META.founderTitleStatus.en}) · Proposed Venue: ${CANONICAL_META.venueName} ${CANONICAL_META.venueBookingStatus.en} · Zero spend without verified RFQs.`}
                  </p>
                </div>
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-4 pt-2">
              <a
                href="#journey"
                className="inline-flex items-center gap-2 px-6 py-3 bg-[#D4AF37] text-[#0B1B3D] font-bold text-sm rounded hover:bg-[#E2C258] transition-colors duration-150 whitespace-nowrap shrink-0"
              >
                <span>
                  {lang === 'ar'
                    ? 'استكشاف رحلة الروبوت KG–G12'
                    : 'Explore KG–G12 Robot Journey'}
                </span>
                <ArrowIcon className="w-4 h-4" aria-hidden="true" />
              </a>

              <a
                href="#governance"
                className="inline-flex items-center gap-2 px-5 py-3 border border-white/30 text-white font-medium text-sm rounded hover:bg-white/10 transition-colors duration-150 whitespace-nowrap shrink-0"
              >
                <CheckSquare className="w-4 h-4 text-[#D4AF37]" aria-hidden="true" />
                <span>
                  {lang === 'ar' ? 'مراجعة القرارات المعلّقة (13)' : 'Review 13 Pending Decisions'}
                </span>
              </a>
            </div>
          </div>

          {/* Visual Showcase Frame */}
          <div className="lg:col-span-5 flex flex-col bg-[#081530] border border-white/15 rounded p-4">
            <div className="flex items-center justify-between gap-2 pb-3 mb-3 border-b border-white/10">
              <span className="text-xs font-medium text-slate-300">
                {lang === 'ar' ? 'الوثائق البصرية المعتمدة' : 'Official Visual Assets'}
              </span>
              <div className="inline-flex items-center gap-1 p-0.5 bg-white/10 rounded">
                {(Object.keys(visualAssets) as Array<keyof typeof visualAssets>).map((key) => (
                  <button
                    key={key}
                    type="button"
                    onClick={() => setActiveVisual(key)}
                    className={`px-2.5 py-1 text-xs rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                      activeVisual === key
                        ? 'bg-[#D4AF37] text-[#0B1B3D] font-bold'
                        : 'text-slate-200 hover:text-white'
                    }`}
                  >
                    {visualAssets[key].label}
                  </button>
                ))}
              </div>
            </div>

            <div className="relative flex-1 min-h-[340px] lg:min-h-[420px] bg-[#0B1B3D] rounded overflow-hidden border border-white/10 flex items-center justify-center">
              {!imgError[activeVisual] ? (
                <img
                  src={currentAsset.src}
                  alt={currentAsset.caption}
                  referrerPolicy="no-referrer"
                  onError={() =>
                    setImgError((prev) => ({ ...prev, [activeVisual]: true }))
                  }
                  className="w-full h-full max-h-[460px] object-contain p-2"
                />
              ) : (
                <div className="p-8 text-center space-y-3">
                  <div className="text-lg font-bold text-[#D4AF37]">Green Grow Bot</div>
                  <p className="text-sm text-slate-300 max-w-xs mx-auto">
                    {currentAsset.caption}
                  </p>
                </div>
              )}
            </div>

            <p className="pt-3 text-xs text-slate-300 leading-relaxed">
              {currentAsset.caption}
            </p>
          </div>
        </div>

        {/* Full-Width 4-Column Operational Fact Strip */}
        <div className="mt-10 pt-8 border-t border-white/15 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="space-y-1">
            <div className="text-xs text-slate-300">
              {lang === 'ar' ? 'النموذج التعليمي التراكمي' : 'Cumulative Progression'}
            </div>
            <div className="text-2xl font-bold text-white tabular-nums">
              {lang === 'ar' ? '9 مراحل (KG1–G12)' : '9 Stages (KG1–G12)'}
            </div>
            <div className="text-xs text-[#E2C258]">
              {lang === 'ar' ? 'التجربة الموصى بها: المرحلة 5 (G6)' : 'Recommended Pilot: Stage 5 (G6)'}
            </div>
          </div>

          <div className="space-y-1">
            <div className="text-xs text-slate-300">
              {lang === 'ar' ? 'هيكل حفل الإطلاق (15 نوفمبر 2026)' : 'Launch Event Format (15 Nov 2026)'}
            </div>
            <div className="text-2xl font-bold text-white tabular-nums">
              {lang === 'ar' ? '85 دقيقة + استقبال' : '85 min + Reception'}
            </div>
            <div className="text-xs text-[#E2C258]">
              {lang === 'ar' ? 'يشمل 12 دقيقة عرضاً عملياً حياً' : 'Includes 12-min live robot demo'}
            </div>
          </div>

          <div className="space-y-1">
            <div className="text-xs text-slate-300">
              {lang === 'ar' ? 'السيناريو A الموصى به (تقدير تخطيط)' : 'Recommended Budget Scenario A (Est.)'}
            </div>
            <div className="text-2xl font-bold text-white tabular-nums ltr-inline text-start">
              164,268 – 191,418 EGP
            </div>
            <div className="text-xs text-[#E2C258]">
              {lang === 'ar' ? 'الحد الأدنى مقابل سقف عدم اليقين +25%' : 'Planning floor vs +25% ceiling'}
            </div>
          </div>

          <div className="space-y-1">
            <div className="text-xs text-slate-300">
              {lang === 'ar' ? 'بوابة الحوكمة والاعتماد' : 'Governance & Risk Gate'}
            </div>
            <div className="text-2xl font-bold text-white tabular-nums">
              {lang === 'ar' ? '13 قراراً · 15 خطراً' : '13 Decisions · 15 Risks'}
            </div>
            <div className="text-xs text-[#E2C258]">
              {lang === 'ar' ? '26 مؤشر قياس (أهداف مبدئية)' : '26 KPIs (Provisional Targets)'}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
