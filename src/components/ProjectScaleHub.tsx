import React, { useState } from 'react';
import { Award, CheckCircle2, Compass, Layers, Users } from 'lucide-react';
import {
  PROJECT_PHASES,
  ROADMAP_36M,
  STAKEHOLDERS,
  SUPPORT_PILLARS,
} from '../data/projectEventData';
import type { Lang } from '../types';

interface ProjectScaleHubProps {
  lang: Lang;
}

export const ProjectScaleHub: React.FC<ProjectScaleHubProps> = ({ lang }) => {
  const [activeTab, setActiveTab] = useState<'pillars' | 'stakeholders' | 'phases' | 'roadmap'>('pillars');
  const [selectedStakeholderId, setSelectedStakeholderId] = useState<string>(STAKEHOLDERS[0].id);

  const selectedStakeholder =
    STAKEHOLDERS.find((s) => s.id === selectedStakeholderId) ?? STAKEHOLDERS[0];

  return (
    <section id="project" className="py-16 lg:py-20 bg-white text-[#0B0F14] border-b border-[#E5E7EB]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 space-y-10">
        {/* Header & Segmented Navigation */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-slate-200">
          <div className="space-y-2 max-w-3xl">
            <div className="text-xs font-bold text-[#2D78FF]">
              {lang === 'ar'
                ? '02. المشروع الشامل والحوكمة التربوية والتوسع (P0–P10)'
                : '02. Full Project Architecture, Governance & 36-Month Scale (P0–P10)'}
            </div>
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#0B1B3D]">
              {lang === 'ar'
                ? 'من التجربة المدرسية إلى مشروع قابل للتكرار والدعم المؤسسي'
                : 'From Pilot Classroom to Replicable Public-Value System'}
            </h2>
            <p className="text-sm sm:text-base text-slate-600 leading-relaxed">
              {lang === 'ar'
                ? 'بنية تنفيذية متكاملة تمتد عبر 11 مرحلة (P0 إلى P10) وخارطة 36 شهراً، مبنية على ست ركائز للاستحقاق العام وتأهيل المعلمين.'
                : 'A structured 11-phase lifecycle (P0–P10) and 36-month roadmap anchored on 6 pillars of public merit and tiered teacher readiness.'}
            </p>
          </div>

          <div className="inline-flex flex-wrap items-center gap-1 p-1 bg-[#FBF9F4] border border-slate-200 rounded shrink-0">
            {(
              [
                { id: 'pillars', ar: 'الأسس الستة', en: '6 Support Pillars' },
                { id: 'stakeholders', ar: 'مصفوفة المعنيين', en: 'Stakeholders' },
                { id: 'phases', ar: 'المراحل P0–P10 وتدريب المعلمين', en: 'P0–P10 & TOT' },
                { id: 'roadmap', ar: 'خارطة 36 شهراً', en: '36-Month Roadmap' },
              ] as const
            ).map((tab) => (
              <button
                key={tab.id}
                type="button"
                onClick={() => setActiveTab(tab.id)}
                className={`px-3.5 py-2 text-xs font-medium rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                  activeTab === tab.id
                    ? 'bg-[#0B1B3D] text-white font-bold'
                    : 'text-slate-700 hover:bg-white'
                }`}
              >
                {lang === 'ar' ? tab.ar : tab.en}
              </button>
            ))}
          </div>
        </div>

        {/* Tab 1: 6 Support Pillars */}
        {activeTab === 'pillars' && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {SUPPORT_PILLARS.map((pillar) => (
              <article
                key={pillar.id}
                className="bg-[#FBF9F4] border border-slate-200 rounded p-6 flex flex-col justify-between space-y-4"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between text-xs font-mono text-slate-500">
                    <span className="font-bold text-[#0B1B3D] tabular-nums">
                      {lang === 'ar' ? `الركيزة 0${pillar.id}` : `Pillar 0${pillar.id}`}
                    </span>
                    <Compass className="w-4 h-4 text-[#D4AF37]" aria-hidden="true" />
                  </div>
                  <h3 className="text-lg font-bold text-[#0B1B3D]">{pillar.title[lang]}</h3>
                  <p className="text-sm text-slate-700 leading-relaxed">{pillar.principle[lang]}</p>
                </div>

                <div className="pt-4 border-t border-slate-200 space-y-2 text-xs">
                  <div>
                    <span className="font-bold text-[#0B1B3D]">
                      {lang === 'ar' ? 'الدليل المطلوب: ' : 'Required Evidence: '}
                    </span>
                    <span className="text-slate-600">{pillar.evidenceRequired[lang]}</span>
                  </div>
                  <div>
                    <span className="font-bold text-[#2D78FF]">
                      {lang === 'ar' ? 'البعد الوطني والمجتمعي: ' : 'National Context: '}
                    </span>
                    <span className="text-slate-600">{pillar.nationalContext[lang]}</span>
                  </div>
                </div>
              </article>
            ))}
          </div>
        )}

        {/* Tab 2: Stakeholder Alignment Matrix */}
        {activeTab === 'stakeholders' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <div className="lg:col-span-4 space-y-2">
              {STAKEHOLDERS.map((st) => {
                const active = st.id === selectedStakeholderId;
                return (
                  <button
                    key={st.id}
                    type="button"
                    onClick={() => setSelectedStakeholderId(st.id)}
                    className={`w-full text-start px-4 py-3.5 rounded border flex items-center justify-between gap-3 transition-colors duration-150 ${
                      active
                        ? 'bg-[#0B1B3D] text-white border-[#0B1B3D] font-bold'
                        : 'bg-[#FBF9F4] text-[#0B0F14] border-slate-200 hover:border-[#2D78FF]'
                    }`}
                  >
                    <span className="text-sm">{st.group[lang]}</span>
                    <Users className={`w-4 h-4 shrink-0 ${active ? 'text-[#D4AF37]' : 'text-slate-400'}`} />
                  </button>
                );
              })}
            </div>

            <div className="lg:col-span-8 bg-[#FBF9F4] border border-slate-200 rounded p-6 sm:p-8 space-y-6">
              <div className="pb-4 border-b border-slate-200">
                <div className="text-xs font-bold text-[#2D78FF]">
                  {lang === 'ar' ? 'ملف أصحاب المصلحة المعتمد' : 'Stakeholder Alignment Profile'}
                </div>
                <h3 className="text-xl font-bold text-[#0B1B3D] mt-1">
                  {selectedStakeholder.group[lang]}
                </h3>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="bg-white border border-slate-200 rounded p-5 space-y-2">
                  <div className="text-xs font-bold text-[#0B1B3D]">
                    {lang === 'ar' ? 'ماذا تحتاج هذه الفئة أن ترى؟' : 'What They Need to See'}
                  </div>
                  <p className="text-sm text-slate-700 leading-relaxed">
                    {selectedStakeholder.needsToSee[lang]}
                  </p>
                </div>

                <div className="bg-white border border-slate-200 rounded p-5 space-y-2">
                  <div className="text-xs font-bold text-amber-700">
                    {lang === 'ar' ? 'ما المخاطر التي تقلقها؟' : 'Key Concerns & Risks'}
                  </div>
                  <p className="text-sm text-slate-700 leading-relaxed">
                    {selectedStakeholder.concerns[lang]}
                  </p>
                </div>

                <div className="bg-white border border-slate-200 rounded p-5 space-y-2">
                  <div className="text-xs font-bold text-[#2D78FF]">
                    {lang === 'ar' ? 'ما الذي نطلبه منها رسمياً؟' : 'Our Formal Ask'}
                  </div>
                  <p className="text-sm text-slate-700 leading-relaxed">
                    {selectedStakeholder.ourAsk[lang]}
                  </p>
                </div>

                <div className="bg-white border border-slate-200 rounded p-5 space-y-2">
                  <div className="text-xs font-bold text-[#059669]">
                    {lang === 'ar' ? 'الدليل الوثائقي الذي نقدمه لها' : 'Verified Evidence Provided'}
                  </div>
                  <p className="text-sm text-slate-700 leading-relaxed">
                    {selectedStakeholder.evidenceProvided[lang]}
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tab 3: Phases P0-P10 + Teacher TOT */}
        {activeTab === 'phases' && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
              {PROJECT_PHASES.map((phase) => (
                <div
                  key={phase.code}
                  className="bg-[#FBF9F4] border border-slate-200 rounded p-5 flex flex-col justify-between space-y-4"
                >
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-xs font-mono">
                      <span className="font-bold text-[#0B1B3D] bg-white px-2 py-0.5 border border-slate-200 rounded">
                        {phase.code}
                      </span>
                      <span className="text-slate-500">{phase.timeframe[lang]}</span>
                    </div>
                    <h3 className="text-base font-bold text-[#0B1B3D]">{phase.title[lang]}</h3>
                    <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
                      {phase.objectives[lang]}
                    </p>
                  </div>

                  <div className="pt-3 border-t border-slate-200 space-y-2 text-xs">
                    <div className="text-slate-600">
                      <span className="font-bold text-[#0B1B3D]">
                        {lang === 'ar' ? 'شرط الانتقال: ' : 'Gate: '}
                      </span>
                      {phase.transitionGate[lang]}
                    </div>
                    <div className="flex flex-wrap items-center justify-between gap-2 text-[11px] text-slate-500">
                      <span>{phase.owner[lang]}</span>
                      <span className="font-mono ltr-inline">{phase.deliverables[0]}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Teacher Training TOT & 60-Min Lesson Structure */}
            <div className="bg-[#0B1B3D] text-white rounded p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-12 gap-8">
              <div className="lg:col-span-6 space-y-4">
                <div className="flex items-center gap-2 text-xs font-bold text-[#D4AF37]">
                  <Award className="w-4 h-4" aria-hidden="true" />
                  <span>
                    {lang === 'ar'
                      ? 'مسار تأهيل المعلمين المتدرج (TOT — 30% شرح / 40% عملي / 30% عرض)'
                      : 'Tiered Teacher Readiness (TOT — 30% Lecture / 40% Lab / 30% Practice)'}
                  </span>
                </div>
                <h3 className="text-xl font-bold">
                  {lang === 'ar'
                    ? 'تحويل دور المعلم من «مُلقِّن» إلى «مهندس تعلّم»'
                    : 'Shifting Educator Role from Lecturer to Learning Engineer'}
                </h3>
                <div className="space-y-3 text-xs sm:text-sm">
                  <div className="p-3 bg-white/8 rounded border border-white/10">
                    <div className="font-bold text-[#E2C258]">
                      T1 — {lang === 'ar' ? 'التأسيس (معلمو KG–G3 · 12 ساعة)' : 'Foundation (KG–G3 · 12 Hours)'}
                    </div>
                    <p className="text-slate-200 mt-1">
                      {lang === 'ar'
                        ? 'تشغيل WhalesBot U20 Pro / WeDo 2.0 + إدارة الحصة الـ 60 دقيقة + قوالب التوثيق والسلامة.'
                        : 'WhalesBot U20 Pro / WeDo 2.0, 60-min class flow & safety/portfolio templates.'}
                    </p>
                  </div>
                  <div className="p-3 bg-white/8 rounded border border-white/10">
                    <div className="font-bold text-[#E2C258]">
                      T2 — {lang === 'ar' ? 'البرمجة والقياس (معلمو G4–G8 · 16 ساعة)' : 'Coding & Sensors (G4–G8 · 16 Hours)'}
                    </div>
                    <p className="text-slate-200 mt-1">
                      {lang === 'ar'
                        ? 'PictoBlox / micro:bit وArduino Uno مع الحساسات + اجتياز اختبار تسجيل 10 قراءات.'
                        : 'PictoBlox / micro:bit & Arduino sensor logging (10-trial calibration pass check).'}
                    </p>
                  </div>
                  <div className="p-3 bg-white/8 rounded border border-white/10">
                    <div className="font-bold text-[#E2C258]">
                      T3 — {lang === 'ar' ? 'الأنظمة والتصميم (معلمو G9–G12 · 16 ساعة)' : 'Systems & CAD (G9–G12 · 16 Hours)'}
                    </div>
                    <p className="text-slate-200 mt-1">
                      {lang === 'ar'
                        ? 'المحاكاة وCAD + ESP32 وMQTT وNode-RED + معايير السلامة الكهربائية واللحام الآمن.'
                        : 'CAD simulation + ESP32/MQTT/Node-RED + electrical & G9+ soldering safety.'}
                    </p>
                  </div>
                </div>
              </div>

              <div className="lg:col-span-6 space-y-4">
                <div className="flex items-center gap-2 text-xs font-bold text-[#D4AF37]">
                  <Layers className="w-4 h-4" aria-hidden="true" />
                  <span>
                    {lang === 'ar'
                      ? 'بنية الحصة التطبيقية المعتمدة (60–75 دقيقة)'
                      : 'Standard Applied Session Cadence (60–75 Minutes)'}
                  </span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                  {[
                    { idx: '01', ar: 'إثارة (5–7 د)', en: 'Spark (5–7m)', descAr: 'طرح مشكلة أو عطل دون شرح الحل', descEn: 'Pose problem without spoiling solution' },
                    { idx: '02', ar: 'استكشاف (8–10 د)', en: 'Explore (8–10m)', descAr: 'تجريب أولي وتساؤلات استقصائية', descEn: 'Hands-on probing & inquiry questions' },
                    { idx: '03', ar: 'بناء (25–30 د)', en: 'Build (25–30m)', descAr: 'تنفيذ مع سجل أخطاء وتوجيه', descEn: 'Iterative construction + bug log' },
                    { idx: '04', ar: 'اختبار (8–10 د)', en: 'Test (8–10m)', descAr: 'قياس الأداء مقابل معايير القبول', descEn: 'Verify against numeric criteria' },
                    { idx: '05', ar: 'توثيق (8–10 د)', en: 'Document (8–10m)', descAr: 'صورة + رقم + سطر تفسير بالملف', descEn: 'Photo + data + 1-line portfolio entry' },
                    { idx: '06', ar: 'عرض (5–7 د)', en: 'Present (5–7m)', descAr: 'عرض صفّي وإجابة سؤال نقدي', descEn: 'Peer presentation & critical Q&A' },
                  ].map((step) => (
                    <div key={step.idx} className="p-3 bg-white/6 border border-white/10 rounded space-y-1">
                      <div className="font-bold text-white flex items-center justify-between">
                        <span>{lang === 'ar' ? step.ar : step.en}</span>
                        <span className="font-mono text-[#D4AF37]">{step.idx}</span>
                      </div>
                      <p className="text-slate-300">{lang === 'ar' ? step.descAr : step.descEn}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tab 4: 36-Month Roadmap (Jan 2027 - Dec 2029) */}
        {activeTab === 'roadmap' && (
          <div className="space-y-4">
            <div className="text-xs text-slate-600">
              {lang === 'ar'
                ? 'تنويه: بداية افتراضية من يناير 2027 تخضع لاعتماد التقويم الدراسي ونتائج حفل 15 نوفمبر 2026، وتُدار عبر 5 بوابات قرار (Go / Adjust / Stop).'
                : 'Note: Indicative timeline starting Jan 2027 subject to approved academic calendar, governed by 5 explicit Go / Adjust / Stop gates.'}
            </div>

            <div className="space-y-4">
              {ROADMAP_36M.map((ms) => (
                <div
                  key={ms.id}
                  className="bg-[#FBF9F4] border border-slate-200 rounded p-5 grid grid-cols-1 lg:grid-cols-12 gap-4 items-center"
                >
                  <div className="lg:col-span-3 space-y-1">
                    <div className="text-xs font-mono text-[#2D78FF] font-bold">{ms.phasesCovered}</div>
                    <div className="text-base font-bold text-[#0B1B3D]">{ms.period[lang]}</div>
                  </div>

                  <div className="lg:col-span-5 text-sm text-slate-700 leading-relaxed">
                    {ms.focus[lang]}
                  </div>

                  <div className="lg:col-span-4 bg-white border border-slate-200 rounded p-3.5 flex items-start gap-2.5">
                    <CheckCircle2 className="w-4 h-4 text-[#059669] shrink-0 mt-0.5" aria-hidden="true" />
                    <div className="text-xs space-y-0.5">
                      <div className="font-bold text-[#0B1B3D] ltr-inline text-start">
                        {ms.gateType}
                      </div>
                      <div className="text-slate-600">{ms.gateCriteria[lang]}</div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  );
};
