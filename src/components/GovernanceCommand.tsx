import React, { useEffect, useState } from 'react';
import {
  AlertOctagon,
  BarChart3,
  Check,
  CheckCircle2,
  Copy,
  FileWarning,
  RotateCcw,
  Shield,
  Wallet,
} from 'lucide-react';
import {
  BASELINE_RESET_ITEMS,
  BUDGET_SCENARIOS,
  EXCLUDED_COSTS,
  HARD_RULES,
  KPI_METRICS,
  PENDING_DECISIONS,
  RISK_REGISTER,
} from '../data/projectEventData';
import type { Lang } from '../types';

interface GovernanceCommandProps {
  lang: Lang;
}

type DecisionState = 'pending' | 'reviewing' | 'draft_ok';

const STORAGE_KEY = 'ggb_pending_decisions_v1';

export const GovernanceCommand: React.FC<GovernanceCommandProps> = ({ lang }) => {
  const [selectedScenarioId, setSelectedScenarioId] = useState<'A' | 'B' | 'C'>('A');
  const [kpiCluster, setKpiCluster] = useState<'ALL' | 'EVT' | 'EXE' | 'COM' | 'EDU'>('ALL');
  const [riskSeverity, setRiskSeverity] = useState<'all' | 'critical' | 'high' | 'medium'>('all');
  const [decisionStatuses, setDecisionStatuses] = useState<Record<number, DecisionState>>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) return JSON.parse(saved) as Record<number, DecisionState>;
    } catch {
      // Ignore storage failures in restricted contexts
    }
    return {};
  });
  const [copiedSummary, setCopiedSummary] = useState(false);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(decisionStatuses));
    } catch {
      // Ignore storage write errors
    }
  }, [decisionStatuses]);

  const scenario =
    BUDGET_SCENARIOS.find((s) => s.id === selectedScenarioId) ?? BUDGET_SCENARIOS[0];

  const visibleKpis =
    kpiCluster === 'ALL'
      ? KPI_METRICS
      : KPI_METRICS.filter((k) => k.cluster === kpiCluster);

  const visibleRisks =
    riskSeverity === 'all'
      ? RISK_REGISTER
      : RISK_REGISTER.filter((r) => r.severity === riskSeverity);

  const reviewedCount = PENDING_DECISIONS.filter(
    (d) => decisionStatuses[d.id] === 'draft_ok'
  ).length;

  const setDecision = (id: number, next: DecisionState) => {
    setDecisionStatuses((prev) => ({ ...prev, [id]: next }));
  };

  const handleCopyDecisionSummary = async () => {
    const lines = PENDING_DECISIONS.map((d) => {
      const st = decisionStatuses[d.id] ?? 'pending';
      const label =
        st === 'draft_ok'
          ? lang === 'ar'
            ? 'مسودة موافقة أولية'
            : 'Draft Approved'
          : st === 'reviewing'
          ? lang === 'ar'
            ? 'قيد المراجعة'
            : 'In Review'
          : lang === 'ar'
          ? 'معلّق'
          : 'Pending';
      return `${d.id}. [${label}] (${d.owner}) ${d.title[lang]}`;
    }).join('\n');

    try {
      await navigator.clipboard.writeText(
        `${lang === 'ar' ? 'ملخص مسودة القرارات الـ 13 (غير موقع رسمياً بعد)' : '13 Pending Decisions Working Summary (Not Official Signature)'}\n\n${lines}`
      );
      setCopiedSummary(true);
      setTimeout(() => setCopiedSummary(false), 2200);
    } catch {
      setCopiedSummary(false);
    }
  };

  const formatEgp = (val: number) => val.toLocaleString('en-US');

  return (
    <section id="governance" className="py-16 lg:py-20 bg-white text-[#0B0F14]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 space-y-14">
        {/* Section Header */}
        <div className="space-y-2 pb-6 border-b border-slate-200 max-w-3xl">
          <div className="text-xs font-bold text-[#2D78FF]">
            {lang === 'ar'
              ? '04. بوابة الحوكمة التنفيذية والميزانية والمخاطر'
              : '04. Executive Governance, Budgets, KPIs & Risk Command'}
          </div>
          <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#0B1B3D]">
            {lang === 'ar'
              ? 'مقارن الميزانيات، سجل القرارات الـ 13، والمؤشرات والمخاطر'
              : 'Budget Scenarios A/B/C, 13 Pending Decisions, 26 KPIs & 15 Risks'}
          </h2>
          <p className="text-sm sm:text-base text-slate-600 leading-relaxed">
            {lang === 'ar'
              ? 'كل الأرقام المالية تقديرات تخطيط أولية بانتظار عروض الأسعار (RFQ)، وكل أهداف الأداء مبدئية حتى يُقاس خط الأساس الفعلي.'
              : 'All financial figures are initial planning estimates awaiting formal RFQs, and all KPI targets are provisional pending empirical baseline capture.'}
          </p>
        </div>

        {/* 1. Nov 10 Baseline Reset Urgent Action Matrix */}
        <div className="bg-amber-50/70 border border-amber-200 rounded p-6 space-y-4">
          <div className="flex items-center gap-2 text-sm font-bold text-amber-950">
            <FileWarning className="w-5 h-5 text-amber-700 shrink-0" aria-hidden="true" />
            <span>
              {lang === 'ar'
                ? 'قاعدة إعادة الضبط الزمني (تحديث 10 نوفمبر 2026 — المتبقي 5 أيام)'
                : 'Nov 10 Baseline Reset Rule (5 Days Remaining to Nov 15)'}
            </span>
          </div>
          <p className="text-xs sm:text-sm text-amber-950 leading-relaxed">
            {lang === 'ar'
              ? 'أي بند لا يمكن إغلاقه كتابياً خلال 24 ساعة يُسقط من النطاق ولا يُستبدل بافتراض؛ وعند تعذر تأكيد الفندق يُحوَّل الاستقبال لقاعة داخلية بالمدرسة.'
              : 'Any item not closed in writing within 24h drops from scope without assumption; if hotel booking stays unconfirmed, relocate reception to an internal GIS hall.'}
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-3">
            {BASELINE_RESET_ITEMS.map((item, idx) => (
              <div key={idx} className="bg-white border border-amber-200 rounded p-3.5 space-y-1.5 text-xs">
                <div className="font-mono font-bold text-[#2D78FF]">{item.owner}</div>
                <div className="font-bold text-[#0B1B3D]">{item.item[lang]}</div>
                <div className="text-amber-800">{item.status[lang]}</div>
                <div className="pt-1 border-t border-amber-100 text-slate-700">
                  {item.action24h[lang]}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 2. Budget Scenario Comparator (A / B / C) */}
        <div className="space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <Wallet className="w-5 h-5 text-[#2D78FF]" aria-hidden="true" />
              <h3 className="text-xl font-bold text-[#0B1B3D]">
                {lang === 'ar'
                  ? 'مقارن سيناريوهات الميزانية (الحد الأدنى مقابل السقف +25%)'
                  : 'Budget Scenario Comparator (Planning Floor vs +25% Ceiling)'}
              </h3>
            </div>

            <div className="inline-flex items-center gap-1 p-1 bg-[#FBF9F4] border border-slate-200 rounded">
              {BUDGET_SCENARIOS.map((sc) => (
                <button
                  key={sc.id}
                  type="button"
                  onClick={() => setSelectedScenarioId(sc.id)}
                  className={`px-3.5 py-1.5 text-xs font-bold rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                    selectedScenarioId === sc.id
                      ? 'bg-[#0B1B3D] text-white'
                      : 'text-slate-700 hover:bg-white'
                  }`}
                >
                  {lang === 'ar'
                    ? `السيناريو ${sc.id}${sc.recommended ? ' ★' : ''}`
                    : `Scenario ${sc.id}${sc.recommended ? ' ★' : ''}`}
                </button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            {/* Detailed Breakdown Table */}
            <div className="lg:col-span-8 bg-[#FBF9F4] border border-slate-200 rounded overflow-hidden">
              <div className="px-5 py-4 bg-white border-b border-slate-200 flex flex-wrap items-center justify-between gap-2">
                <div>
                  <div className="font-bold text-base text-[#0B1B3D]">{scenario.name[lang]}</div>
                  <div className="text-xs text-slate-600 mt-0.5">
                    {scenario.room[lang]} · {scenario.invites}{' '}
                    {lang === 'ar' ? 'دعوة' : 'invites'} · {scenario.attendance}{' '}
                    {lang === 'ar' ? 'حضور متوقع' : 'expected'}
                  </div>
                </div>
                <span className="text-xs font-mono text-amber-800 font-semibold">
                  {lang === 'ar' ? 'تقدير تخطيط (ج.م)' : 'Planning Estimate (EGP)'}
                </span>
              </div>

              <div className="divide-y divide-slate-200 bg-white">
                {scenario.items.map((row) => (
                  <div
                    key={row.id}
                    className="px-5 py-3 grid grid-cols-12 gap-3 items-center text-xs sm:text-sm"
                  >
                    <div className="col-span-6 sm:col-span-7 font-medium text-[#0B0F14]">
                      <span className="font-mono text-slate-400 me-2 tabular-nums">
                        0{row.id}.
                      </span>
                      {row.name[lang]}
                    </div>
                    <div className="col-span-3 text-xs text-slate-600">
                      {row.basis[lang]}
                    </div>
                    <div className="col-span-3 sm:col-span-2 text-end font-mono font-bold text-[#0B1B3D] tabular-nums ltr-inline">
                      {formatEgp(row.amount)}
                    </div>
                  </div>
                ))}
              </div>

              {/* Totals Footer */}
              <div className="p-5 bg-[#0B1B3D] text-white grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
                <div>
                  <div className="text-slate-300">
                    {lang === 'ar'
                      ? `إجمالي 1–9 + احتياطي (${scenario.contingencyRate}%)`
                      : `Items 1–9 + Contingency (${scenario.contingencyRate}%)`}
                  </div>
                  <div className="text-lg font-bold font-mono tabular-nums mt-0.5 ltr-inline text-start">
                    {formatEgp(scenario.floorTotal)} EGP
                  </div>
                  <div className="text-[11px] text-slate-300">
                    {lang === 'ar' ? 'الحد الأدنى للتخطيط (Floor)' : 'Planning Floor'}
                  </div>
                </div>
                <div>
                  <div className="text-slate-300">
                    {lang === 'ar'
                      ? 'هامش عدم اليقين +25% (للبنود 1،2،6،7)'
                      : '+25% Uncertainty (Unpriced 1,2,6,7)'}
                  </div>
                  <div className="text-lg font-bold font-mono tabular-nums text-[#E2C258] mt-0.5 ltr-inline text-start">
                    +{formatEgp(scenario.uncertaintyMargin25)} EGP
                  </div>
                  <div className="text-[11px] text-slate-300">
                    {lang === 'ar' ? `على أساس ${formatEgp(scenario.unpricedBase)} ج.م` : `On ${formatEgp(scenario.unpricedBase)} base`}
                  </div>
                </div>
                <div>
                  <div className="text-slate-300">
                    {lang === 'ar' ? 'السقف المعتمد للاعتماد' : 'Approved Spending Ceiling'}
                  </div>
                  <div className="text-xl font-bold font-mono tabular-nums text-[#D4AF37] mt-0.5 ltr-inline text-start">
                    {formatEgp(scenario.ceilingTotal)} EGP
                  </div>
                  <div className="text-[11px] text-slate-300">
                    {lang === 'ar' ? 'يُستبدل بعروض RFQ الفعلية' : 'Replaced by live RFQ quotes'}
                  </div>
                </div>
              </div>
            </div>

            {/* Side Comparison & Excluded Costs */}
            <div className="lg:col-span-4 space-y-5">
              <div className="bg-[#FBF9F4] border border-slate-200 rounded p-5 space-y-3">
                <div className="text-sm font-bold text-[#0B1B3D]">
                  {lang === 'ar' ? 'مقارنة سريعة للسيناريوهات الثلاثة' : 'Quick 3-Scenario Comparison'}
                </div>
                {BUDGET_SCENARIOS.map((sc) => (
                  <button
                    key={sc.id}
                    type="button"
                    onClick={() => setSelectedScenarioId(sc.id)}
                    className={`w-full text-start p-3 rounded border transition-colors text-xs space-y-1 ${
                      sc.id === selectedScenarioId
                        ? 'bg-[#0B1B3D] text-white border-[#0B1B3D]'
                        : 'bg-white text-[#0B0F14] border-slate-200 hover:border-[#2D78FF]'
                    }`}
                  >
                    <div className="flex justify-between font-bold">
                      <span>{sc.name[lang]}</span>
                      <span className="font-mono tabular-nums">{sc.attendance}</span>
                    </div>
                    <div className="font-mono tabular-nums opacity-85 ltr-inline text-start">
                      Floor: {formatEgp(sc.floorTotal)} · Ceiling: {formatEgp(sc.ceilingTotal)} EGP
                    </div>
                  </button>
                ))}
              </div>

              <div className="bg-[#FBF9F4] border border-slate-200 rounded p-5 space-y-2.5">
                <div className="text-xs font-bold text-red-800">
                  {lang === 'ar' ? 'بنود تكلفة خارج النطاق (مستبعدة صراحةً):' : 'Explicitly Excluded Costs:'}
                </div>
                <ul className="space-y-1.5 text-xs text-slate-700 list-disc list-inside leading-relaxed">
                  {EXCLUDED_COSTS[lang].map((ex, i) => (
                    <li key={i}>{ex}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* 3. 13 Pending Executive Decisions Interactive Tracker */}
        <div className="bg-[#FBF9F4] border border-slate-200 rounded p-6 sm:p-8 space-y-6">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-200">
            <div className="space-y-1">
              <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
                <CheckCircle2 className="w-5 h-5 text-[#2D78FF]" aria-hidden="true" />
                <span>
                  {lang === 'ar'
                    ? `سجل القرارات المعلّقة الـ 13 (مسودة مراجعة: ${reviewedCount} / 13)`
                    : `13 Pending Executive Decisions Tracker (Draft Reviewed: ${reviewedCount} / 13)`}
                </span>
              </div>
              <p className="text-xs text-slate-600">
                {lang === 'ar'
                  ? 'أداة مساعدة لتجهيز مسودة الاعتماد محلياً للأستاذ أحمد جبر وفريق المشروع (لا تُغني عن التوقيع الرسمي الموثق).'
                  : 'Local working draft assistant for Mr. Ahmed Gabr & PM team (does not replace formal signed approval).'}
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-2">
              <button
                type="button"
                onClick={handleCopyDecisionSummary}
                className="inline-flex items-center gap-1.5 px-3.5 py-2 text-xs font-bold bg-[#0B1B3D] text-white rounded hover:bg-[#132957] transition-colors"
              >
                {copiedSummary ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                <span>
                  {copiedSummary
                    ? lang === 'ar'
                      ? 'تم نسخ الملخص'
                      : 'Summary Copied'
                    : lang === 'ar'
                    ? 'نسخ مسودة القرارات'
                    : 'Copy Working Summary'}
                </span>
              </button>
              <button
                type="button"
                onClick={() => setDecisionStatuses({})}
                className="inline-flex items-center gap-1.5 px-3 py-2 text-xs font-medium bg-white border border-slate-200 text-slate-700 rounded hover:bg-slate-50 transition-colors"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>{lang === 'ar' ? 'إعادة ضبط' : 'Reset'}</span>
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {PENDING_DECISIONS.map((dec) => {
              const current = decisionStatuses[dec.id] ?? 'pending';
              return (
                <div
                  key={dec.id}
                  className="bg-white border border-slate-200 rounded p-4 flex flex-col justify-between gap-3"
                >
                  <div className="space-y-1">
                    <div className="flex items-center justify-between gap-2 text-xs font-mono">
                      <span className="font-bold text-[#0B1B3D]">
                        #{dec.id.toString().padStart(2, '0')} · {dec.owner}
                      </span>
                      <span
                        className={`font-semibold ${
                          dec.urgency === 'critical'
                            ? 'text-red-700'
                            : dec.urgency === 'high'
                            ? 'text-amber-700'
                            : 'text-slate-500'
                        }`}
                      >
                        {dec.urgency === 'critical'
                          ? lang === 'ar'
                            ? 'أولوية قصوى'
                            : 'Critical'
                          : dec.urgency === 'high'
                          ? lang === 'ar'
                            ? 'عالية'
                            : 'High'
                          : lang === 'ar'
                          ? 'قياسية'
                          : 'Standard'}
                      </span>
                    </div>
                    <div className="text-sm font-bold text-[#0B0F14]">{dec.title[lang]}</div>
                    <div className="text-xs text-slate-600">
                      <span className="font-semibold text-[#0B1B3D]">
                        {lang === 'ar' ? 'الافتراضي المقترح: ' : 'Default Path: '}
                      </span>
                      {dec.defaultIfPending[lang]}
                    </div>
                  </div>

                  <div className="inline-flex items-center gap-1 p-1 bg-slate-100 rounded self-start">
                    {(
                      [
                        { id: 'pending', ar: 'معلّق', en: 'Pending' },
                        { id: 'reviewing', ar: 'للمراجعة', en: 'Reviewing' },
                        { id: 'draft_ok', ar: 'مسودة موافقة', en: 'Draft Ready' },
                      ] as const
                    ).map((opt) => (
                      <button
                        key={opt.id}
                        type="button"
                        onClick={() => setDecision(dec.id, opt.id)}
                        className={`px-2.5 py-1 text-[11px] font-medium rounded transition-colors ${
                          current === opt.id
                            ? opt.id === 'draft_ok'
                              ? 'bg-[#059669] text-white font-bold'
                              : opt.id === 'reviewing'
                              ? 'bg-[#2D78FF] text-white font-bold'
                              : 'bg-white text-[#0B1B3D] font-bold shadow-xs'
                            : 'text-slate-600 hover:text-[#0B1B3D]'
                        }`}
                      >
                        {lang === 'ar' ? opt.ar : opt.en}
                      </button>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 4. 26 Canonical KPIs Matrix */}
        <div className="space-y-5">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <BarChart3 className="w-5 h-5 text-[#2D78FF]" aria-hidden="true" />
                <h3 className="text-xl font-bold text-[#0B1B3D]">
                  {lang === 'ar'
                    ? 'مؤشرات الأداء الـ 26 (جميع الأهداف «مبدئية» بانتظار القياس)'
                    : '26 Canonical KPIs (All Targets Provisional Until Baseline)'}
                </h3>
              </div>
              <p className="text-xs text-red-800 font-medium">
                {lang === 'ar'
                  ? 'قاعدة COM-09: لا يُنسب أي تحسن في القيمة السوقية للمدرسة إلى الحفل؛ ما يُنسب هو مسار التحويل (استفسار ← زيارة ← تقديم ← تسجيل) فقط.'
                  : 'COM-09 Rule: School valuation is strictly isolated from event attribution; only conversion funnel metrics (Inquiry -> Tour -> Apply -> Enroll) apply.'}
              </p>
            </div>

            <div className="inline-flex flex-wrap items-center gap-1 p-1 bg-[#FBF9F4] border border-slate-200 rounded shrink-0">
              {(
                [
                  { id: 'ALL', ar: 'الكل (26)', en: 'All (26)' },
                  { id: 'EVT', ar: 'الحفل (EVT)', en: 'Event (EVT)' },
                  { id: 'EXE', ar: 'التنفيذ (EXE)', en: 'Exec (EXE)' },
                  { id: 'COM', ar: 'التحويل (COM)', en: 'Funnel (COM)' },
                  { id: 'EDU', ar: 'التعلم كيركباتريك (EDU)', en: 'Kirkpatrick (EDU)' },
                ] as const
              ).map((c) => (
                <button
                  key={c.id}
                  type="button"
                  onClick={() => setKpiCluster(c.id)}
                  className={`px-3 py-1.5 text-xs font-medium rounded transition-colors whitespace-nowrap shrink-0 ${
                    kpiCluster === c.id
                      ? 'bg-[#0B1B3D] text-white font-bold'
                      : 'text-slate-700 hover:bg-white'
                  }`}
                >
                  {lang === 'ar' ? c.ar : c.en}
                </button>
              ))}
            </div>
          </div>

          <div className="overflow-x-auto border border-slate-200 rounded">
            <table className="w-full text-start border-collapse text-xs sm:text-sm">
              <thead className="bg-[#0B1B3D] text-white text-xs">
                <tr>
                  <th className="p-3 text-start font-bold">ID</th>
                  <th className="p-3 text-start font-bold">{lang === 'ar' ? 'المؤشر' : 'Metric'}</th>
                  <th className="p-3 text-start font-bold">{lang === 'ar' ? 'المعادلة / المصدر' : 'Formula'}</th>
                  <th className="p-3 text-start font-bold">{lang === 'ar' ? 'المسؤول' : 'Owner'}</th>
                  <th className="p-3 text-start font-bold">{lang === 'ar' ? 'خط الأساس' : 'Baseline'}</th>
                  <th className="p-3 text-start font-bold">{lang === 'ar' ? 'الهدف المبدئي' : 'Provisional Target'}</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 bg-white">
                {visibleKpis.map((kpi) => (
                  <tr key={kpi.id} className="hover:bg-[#FBF9F4]">
                    <td className="p-3 font-mono font-bold text-[#2D78FF] whitespace-nowrap ltr-inline">
                      {kpi.id}
                      {kpi.levelNote ? ` · ${kpi.levelNote}` : ''}
                    </td>
                    <td className="p-3 font-bold text-[#0B1B3D]">{kpi.name[lang]}</td>
                    <td className="p-3 text-slate-600">{kpi.formula[lang]}</td>
                    <td className="p-3 text-slate-700">{kpi.owner[lang]}</td>
                    <td className="p-3 font-mono tabular-nums text-slate-500">{kpi.baseline[lang]}</td>
                    <td className="p-3 font-semibold text-[#0B1B3D] tabular-nums">
                      {kpi.provisionalTarget[lang]}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* 5. 15 Risk Register */}
        <div className="space-y-5">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <AlertOctagon className="w-5 h-5 text-red-700" aria-hidden="true" />
              <h3 className="text-xl font-bold text-[#0B1B3D]">
                {lang === 'ar' ? 'سجل المخاطر المعتمد (RSK-01 إلى RSK-15)' : 'Canonical Risk Register (RSK-01 to RSK-15)'}
              </h3>
            </div>
            <div className="inline-flex items-center gap-1 p-1 bg-[#FBF9F4] border border-slate-200 rounded shrink-0">
              {(
                [
                  { id: 'all', ar: 'الكل (15)', en: 'All (15)' },
                  { id: 'critical', ar: 'حرجة', en: 'Critical' },
                  { id: 'high', ar: 'مرتفعة', en: 'High' },
                  { id: 'medium', ar: 'متوسطة', en: 'Medium' },
                ] as const
              ).map((sev) => (
                <button
                  key={sev.id}
                  type="button"
                  onClick={() => setRiskSeverity(sev.id)}
                  className={`px-3 py-1.5 text-xs font-medium rounded transition-colors whitespace-nowrap shrink-0 ${
                    riskSeverity === sev.id
                      ? 'bg-[#0B1B3D] text-white font-bold'
                      : 'text-slate-700 hover:bg-white'
                  }`}
                >
                  {lang === 'ar' ? sev.ar : sev.en}
                </button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {visibleRisks.map((risk) => (
              <div
                key={risk.id}
                className="bg-[#FBF9F4] border border-slate-200 rounded p-4 flex flex-col justify-between space-y-3 text-xs"
              >
                <div className="space-y-1.5">
                  <div className="flex items-center justify-between font-mono">
                    <span className="font-bold text-[#0B1B3D]">{risk.id}</span>
                    <span
                      className={`font-bold ${
                        risk.severity === 'critical'
                          ? 'text-red-700'
                          : risk.severity === 'high'
                          ? 'text-amber-700'
                          : 'text-slate-600'
                      }`}
                    >
                      {risk.severity === 'critical'
                        ? lang === 'ar'
                          ? 'درجة حرجة'
                          : 'CRITICAL'
                        : risk.severity === 'high'
                        ? lang === 'ar'
                          ? 'درجة مرتفعة'
                          : 'HIGH'
                        : lang === 'ar'
                        ? 'درجة متوسطة'
                        : 'MEDIUM'}
                    </span>
                  </div>
                  <div className="text-sm font-bold text-[#0B1B3D]">{risk.title[lang]}</div>
                  <div className="text-slate-600">
                    <span className="font-bold text-[#0B0F14]">
                      {lang === 'ar' ? 'الوقاية: ' : 'Prevention: '}
                    </span>
                    {risk.prevention[lang]}
                  </div>
                  <div className="text-slate-700">
                    <span className="font-bold text-[#2D78FF]">
                      {lang === 'ar' ? 'الاستجابة: ' : 'Response: '}
                    </span>
                    {risk.response[lang]}
                  </div>
                </div>
                <div className="pt-2 border-t border-slate-200 flex justify-between text-[11px] text-slate-500">
                  <span>{risk.owner[lang]}</span>
                  <span>{risk.earlyWarning[lang]}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 6. Non-Negotiable Hard Rules Charter */}
        <div className="bg-[#0B1B3D] text-white rounded p-6 sm:p-8 space-y-4">
          <div className="flex items-center gap-2 text-sm font-bold text-[#D4AF37]">
            <Shield className="w-5 h-5" aria-hidden="true" />
            <span>
              {lang === 'ar'
                ? 'ميثاق القواعد الحاكمة غير القابلة للتجاوز'
                : 'Non-Negotiable Governance & Ethics Charter'}
            </span>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {HARD_RULES.map((rule) => (
              <div key={rule.id} className="p-4 bg-white/6 border border-white/10 rounded text-xs sm:text-sm leading-relaxed text-slate-100">
                <span className="font-mono font-bold text-[#D4AF37] me-1.5">0{rule.id}.</span>
                {rule[lang]}
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};
