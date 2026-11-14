import React, { useMemo, useState } from 'react';
import {
  Activity,
  AlertTriangle,
  BookOpen,
  Cpu,
  Plus,
  RotateCcw,
  ShieldCheck,
  Sliders,
} from 'lucide-react';
import { EDUCATIONAL_STAGES } from '../data/stagesData';
import type { Lang, SchoolFormat } from '../types';

interface RobotJourneyExplorerProps {
  lang: Lang;
}

export const RobotJourneyExplorer: React.FC<RobotJourneyExplorerProps> = ({ lang }) => {
  const [selectedStageId, setSelectedStageId] = useState<number>(5); // Stage 5 (G6) recommended pilot default
  const [schoolFormat, setSchoolFormat] = useState<SchoolFormat>('international');

  // Stage-specific interactive simulator states
  const [pushForce, setPushForce] = useState<number>(6); // Stages 1-2
  const [inclineAngle, setInclineAngle] = useState<number>(12); // Stages 1-2
  const [circuitClosed, setCircuitClosed] = useState<boolean>(true); // Stage 3
  const [ledBonus, setLedBonus] = useState<number>(4); // Stage 3
  const [obstacleDist, setObstacleDist] = useState<number>(22); // Stage 4
  const [sensorDistance, setSensorDistance] = useState<number>(34); // Stage 5 (G6 HC-SR04)
  const [sampleReadings, setSampleReadings] = useState<number[]>([32, 34, 33, 35, 34, 36, 33, 34]);
  const [pwmDuty, setPwmDuty] = useState<number>(65); // Stage 6 (L298N)
  const [tankTarget, setTankTarget] = useState<number>(75); // Stage 6 & 8
  const [cadTolerance, setCadTolerance] = useState<number>(0.5); // Stage 7
  const [mqttLive, setMqttLive] = useState<boolean>(true); // Stage 8
  const [rubricScores, setRubricScores] = useState({
    design: 21,
    build: 20,
    code: 22,
    docs: 19,
  }); // Stage 9

  const stage = useMemo(
    () => EDUCATIONAL_STAGES.find((s) => s.id === selectedStageId) ?? EDUCATIONAL_STAGES[0],
    [selectedStageId]
  );

  // Derived G6 sample statistics
  const g6Stats = useMemo(() => {
    if (sampleReadings.length === 0) return { mean: '0.0', range: '0' };
    const sum = sampleReadings.reduce((acc, v) => acc + v, 0);
    const min = Math.min(...sampleReadings);
    const max = Math.max(...sampleReadings);
    return {
      mean: (sum / sampleReadings.length).toFixed(1),
      range: (max - min).toString(),
    };
  }, [sampleReadings]);

  const handleLogReading = () => {
    setSampleReadings((prev) => {
      const next = [...prev, sensorDistance];
      return next.length > 10 ? next.slice(next.length - 10) : next;
    });
  };

  // Derived Stage 9 rubric total & tier
  const totalRubric =
    rubricScores.design + rubricScores.build + rubricScores.code + rubricScores.docs;
  const rubricTier =
    totalRubric >= 88
      ? { ar: 'يبتكر', en: 'Innovating' }
      : totalRubric >= 75
      ? { ar: 'يتقن', en: 'Proficient' }
      : totalRubric >= 55
      ? { ar: 'يتطور', en: 'Developing' }
      : { ar: 'يبدأ', en: 'Emerging' };

  // Derived Stage 1-2 travel distance (educational model approximation)
  const travelDistanceCm = Math.max(
    10,
    Math.round(pushForce * 14 - inclineAngle * 1.8)
  );

  // Derived Stage 6 pump flow & ACS712 current estimate
  const pumpFlowLpm = ((pwmDuty / 100) * 2.4).toFixed(2);
  const motorCurrentMa = Math.round(140 + pwmDuty * 6.2);

  return (
    <section id="journey" className="py-16 lg:py-20 bg-[#FBF9F4] text-[#0B0F14] border-b border-[#E5E7EB]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 space-y-10">
        {/* Section Header */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-[#0B1B3D]/15">
          <div className="space-y-2 max-w-3xl">
            <div className="text-xs font-bold text-[#2D78FF]">
              {lang === 'ar'
                ? '01. المستكشف التفاعلي للرحلة التراكمية (KG1 إلى Grade 12)'
                : '01. Interactive Cumulative Journey Explorer (KG1 to Grade 12)'}
            </div>
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#0B1B3D]">
              {lang === 'ar'
                ? 'مشروع واحد يتطور مع الطالب عبر 9 مراحل تعليمية'
                : 'One Project Evolving Across 9 Educational Stages'}
            </h2>
            <p className="text-sm sm:text-base text-slate-600 leading-relaxed">
              {lang === 'ar'
                ? 'تتبّع كيف يتدرج «روبوت ترشيد المياه في المدرسة» من عربة دفع بسيطة في الروضة إلى نظام إنترنت أشياء ومشروع تخرج متكامل في الصف الثاني عشر دون تكرار أو انفصال عن المنهج.'
                : 'Trace how the "School Water-Conservation Robot" grows from a push-driven cart in KG/G1 to an ESP32 IoT telemetry system and G12 Capstone without replacing core academics.'}
            </p>
          </div>

          {/* 3 Delivery Format Selector */}
          <div className="space-y-1.5 shrink-0">
            <div className="text-xs font-medium text-slate-600">
              {lang === 'ar' ? 'صيغة التشغيل المدرسية:' : 'School Delivery Format:'}
            </div>
            <div className="inline-flex flex-wrap items-center gap-1 p-1 bg-white border border-slate-200 rounded">
              {(
                [
                  { id: 'international', ar: 'الخاصة / الدولية', en: 'Private / Intl' },
                  { id: 'public_lite', ar: 'العامة الخفيفة', en: 'Public Low-Cost' },
                  { id: 'community', ar: 'أندية المجتمع', en: 'Community Club' },
                ] as const
              ).map((fmt) => (
                <button
                  key={fmt.id}
                  type="button"
                  onClick={() => setSchoolFormat(fmt.id)}
                  className={`px-3 py-1.5 text-xs font-medium rounded transition-colors duration-150 whitespace-nowrap shrink-0 ${
                    schoolFormat === fmt.id
                      ? 'bg-[#0B1B3D] text-white font-bold'
                      : 'text-slate-700 hover:bg-slate-100'
                  }`}
                >
                  {lang === 'ar' ? fmt.ar : fmt.en}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* 9-Stage Horizontal Progression Rail */}
        <div
          role="tablist"
          aria-label={lang === 'ar' ? 'مراحل الرحلة التعليمية التسع' : 'Nine Educational Stages'}
          className="grid grid-cols-3 sm:grid-cols-5 lg:grid-cols-9 gap-2"
        >
          {EDUCATIONAL_STAGES.map((st) => {
            const active = st.id === selectedStageId;
            return (
              <button
                key={st.id}
                type="button"
                role="tab"
                aria-selected={active}
                onClick={() => setSelectedStageId(st.id)}
                className={`text-start p-3 rounded border transition-colors duration-150 flex flex-col justify-between min-h-[84px] ${
                  active
                    ? 'bg-[#0B1B3D] text-white border-[#0B1B3D]'
                    : 'bg-white text-[#0B0F14] border-slate-200 hover:border-[#2D78FF]'
                }`}
              >
                <div className="flex items-center justify-between gap-1 text-xs font-mono tabular-nums">
                  <span className={active ? 'text-[#D4AF37] font-bold' : 'text-slate-500'}>
                    0{st.id}
                  </span>
                  <span className="font-bold ltr-inline">{st.gradeCode}</span>
                </div>
                <div className="text-xs font-bold leading-snug line-clamp-2 mt-1">
                  {st.title[lang]}
                </div>
                {st.isRecommendedPilot && (
                  <div
                    className={`text-[11px] font-medium mt-1 ${
                      active ? 'text-[#E2C258]' : 'text-[#2D78FF]'
                    }`}
                  >
                    {lang === 'ar' ? 'بداية التجربة ★' : 'Pilot Entry ★'}
                  </div>
                )}
              </button>
            );
          })}
        </div>

        {/* Two-Zone Educational Sandbox (Left/Top Stage Canvas + Right/Bottom Interactive Control Deck) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          {/* Interactive Simulation Stage (60-65% width) */}
          <div className="lg:col-span-7 bg-[#0B1B3D] text-white rounded border border-[#0B1B3D] p-6 flex flex-col justify-between">
            <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-white/15">
              <div>
                <div className="text-xs text-[#E2C258] font-medium flex flex-wrap items-center gap-2">
                  <span>
                    {lang === 'ar' ? `المرحلة ${stage.id}` : `Stage ${stage.id}`}
                  </span>
                  <span aria-hidden="true">·</span>
                  <span className="ltr-inline">{stage.gradeCode}</span>
                  <span aria-hidden="true">·</span>
                  <span className="tabular-nums">
                    {lang === 'ar' ? `${stage.ageRange} سنوات` : `Ages ${stage.ageRange}`}
                  </span>
                </div>
                <h3 className="text-xl font-bold text-white mt-1">
                  {lang === 'ar'
                    ? 'محاكي المسار الموحّد: روبوت ترشيد المياه في المدرسة'
                    : 'Unified Worked Example: School Water-Conservation Robot'}
                </h3>
              </div>
              <span className="text-xs font-mono text-slate-300 tabular-nums">
                {stage.platform[lang]}
              </span>
            </div>

            {/* Dynamic Responsive SVG Schematic per Stage */}
            <div className="my-6 bg-[#061026] border border-white/10 rounded p-4 sm:p-6">
              <svg
                viewBox="0 0 640 250"
                className="w-full h-auto max-h-[270px]"
                role="img"
                aria-label={stage.waterBotStep[lang]}
              >
                {/* Technical Grid */}
                <defs>
                  <pattern id="gridPattern" width="32" height="32" patternUnits="userSpaceOnUse">
                    <path
                      d="M 32 0 L 0 0 0 32"
                      fill="none"
                      stroke="rgba(255,255,255,0.05)"
                      strokeWidth="1"
                    />
                  </pattern>
                </defs>
                <rect width="640" height="250" fill="url(#gridPattern)" />

                {/* Ground Track / Incline */}
                <line
                  x1="36"
                  y1="210"
                  x2="604"
                  y2={stage.id <= 2 ? 210 - inclineAngle * 1.4 : 210}
                  stroke="#D4AF37"
                  strokeWidth="2"
                  strokeDasharray="6 4"
                />

                {/* Water Reservoir Tank (Visible & evolving across stages) */}
                <g transform="translate(460, 48)">
                  <rect
                    x="0"
                    y="0"
                    width="130"
                    height="135"
                    rx="4"
                    fill="#0B1B3D"
                    stroke="#E5E7EB"
                    strokeWidth="1.5"
                  />
                  {/* Dynamic Water Fill Level */}
                  {(() => {
                    const fillPct =
                      stage.id === 5
                        ? Math.max(10, Math.min(95, 100 - sensorDistance))
                        : stage.id === 6 || stage.id === 8
                        ? tankTarget
                        : 58;
                    const fillH = Math.round((fillPct / 100) * 115);
                    return (
                      <rect
                        x="4"
                        y={131 - fillH}
                        width="122"
                        height={fillH}
                        fill="#2D78FF"
                        fillOpacity="0.65"
                      />
                    );
                  })()}
                  <text
                    x="65"
                    y="22"
                    textAnchor="middle"
                    fill="#FFFFFF"
                    fontSize="11"
                    fontFamily="IBM Plex Mono, monospace"
                  >
                    WATER TANK
                  </text>
                  <text
                    x="65"
                    y="78"
                    textAnchor="middle"
                    fill="#FFFFFF"
                    fontSize="16"
                    fontWeight="700"
                    fontFamily="IBM Plex Mono, monospace"
                  >
                    {stage.id === 5
                      ? `${sensorDistance} cm`
                      : stage.id === 6 || stage.id === 8
                      ? `${tankTarget}%`
                      : stage.id === 3
                      ? circuitClosed
                        ? 'ON'
                        : 'OFF'
                      : `STG-0${stage.id}`}
                  </text>
                </g>

                {/* Robot Chassis (Position responds to Stage 1-2 force/distance or stays anchored for electronics) */}
                {(() => {
                  const robotX =
                    stage.id <= 2
                      ? 70 + Math.min(260, travelDistanceCm * 1.8)
                      : stage.id === 4
                      ? 90 + Math.min(180, (50 - obstacleDist) * 3)
                      : 110;
                  const robotY =
                    stage.id <= 2 ? 142 - inclineAngle * 0.7 : 142;

                  return (
                    <g transform={`translate(${robotX}, ${robotY})`}>
                      {/* Chassis Body */}
                      <rect
                        x="0"
                        y="0"
                        width="148"
                        height="52"
                        rx="6"
                        fill="#132957"
                        stroke="#D4AF37"
                        strokeWidth="2"
                      />
                      {/* Wheels */}
                      <circle cx="30" cy="56" r="14" fill="#0B0F14" stroke="#E5E7EB" strokeWidth="2.5" />
                      <circle cx="118" cy="56" r="14" fill="#0B0F14" stroke="#E5E7EB" strokeWidth="2.5" />
                      <circle cx="30" cy="56" r="4" fill="#D4AF37" />
                      <circle cx="118" cy="56" r="4" fill="#D4AF37" />

                      {/* Microcontroller / Module Layer (G3+) */}
                      {stage.id >= 3 && (
                        <rect
                          x="18"
                          y="-18"
                          width="70"
                          height="18"
                          rx="2"
                          fill={stage.id >= 8 ? '#2D78FF' : '#059669'}
                          stroke="#FFFFFF"
                          strokeWidth="1"
                        />
                      )}
                      {stage.id >= 3 && (
                        <text
                          x="53"
                          y="-6"
                          textAnchor="middle"
                          fill="#FFFFFF"
                          fontSize="9"
                          fontFamily="IBM Plex Mono, monospace"
                        >
                          {stage.id >= 8
                            ? 'ESP32 Wi-Fi'
                            : stage.id >= 5
                            ? 'Arduino Uno'
                            : 'micro:bit'}
                        </text>
                      )}

                      {/* Alert LED (G3+) */}
                      {stage.id >= 3 && (
                        <circle
                          cx="126"
                          cy="16"
                          r="7"
                          fill={
                            stage.id === 3
                              ? circuitClosed
                                ? '#D4AF37'
                                : '#334155'
                              : stage.id === 4 && obstacleDist < 20
                              ? '#DC2626'
                              : '#22C55E'
                          }
                          stroke="#FFFFFF"
                          strokeWidth="1.2"
                        />
                      )}

                      {/* Ultrasonic Waves (G4-G6) */}
                      {stage.id >= 4 && stage.id <= 6 && (
                        <g stroke="#2D78FF" strokeWidth="1.5" fill="none">
                          <path d="M 156 16 Q 168 26 156 36" />
                          <path d="M 166 10 Q 182 26 166 42" opacity="0.65" />
                        </g>
                      )}

                      {/* Pump / Motor Flow Line (G7+) */}
                      {stage.id >= 6 && (
                        <line
                          x1="148"
                          y1="26"
                          x2="350"
                          y2="26"
                          stroke={pwmDuty > 0 ? '#2D78FF' : '#64748B'}
                          strokeWidth={Math.max(2, Math.round(pwmDuty / 22))}
                          strokeDasharray={stage.id >= 8 && mqttLive ? '6 4' : undefined}
                        />
                      )}

                      <text
                        x="74"
                        y="31"
                        textAnchor="middle"
                        fill="#FFFFFF"
                        fontSize="11"
                        fontWeight="700"
                        fontFamily="IBM Plex Mono, monospace"
                      >
                        GREEN GROW BOT
                      </text>
                    </g>
                  );
                })()}

                {/* Telemetry / Stage Signal Tag */}
                <text
                  x="36"
                  y="30"
                  fill="#D4AF37"
                  fontSize="12"
                  fontWeight="700"
                  fontFamily="IBM Plex Mono, monospace"
                >
                  {stage.id === 8
                    ? `MQTT TOPIC: gis/obour/waterbot · ${mqttLive ? 'STREAMING' : 'PAUSED'}`
                    : stage.id === 9
                    ? `CAPSTONE SCORE: ${totalRubric}/100 (${rubricTier.en.toUpperCase()})`
                    : `STAGE 0${stage.id} · ${stage.gradeCode} · ACTIVE MODEL`}
                </text>
              </svg>
            </div>

            <div className="bg-white/6 border border-white/15 rounded p-4 space-y-1.5">
              <div className="text-xs font-bold text-[#D4AF37]">
                {lang === 'ar'
                  ? 'دور هذه المرحلة في مثال «روبوت ترشيد المياه»:'
                  : 'Stage Role in the Water-Conservation Robot:'}
              </div>
              <p className="text-sm text-slate-100 leading-relaxed">
                {stage.waterBotStep[lang]}
              </p>
            </div>
          </div>

          {/* Right/End Interactive Control & Concept Deck (35-40% width) */}
          <div className="lg:col-span-5 bg-white border border-slate-200 rounded p-6 flex flex-col justify-between space-y-6">
            <div className="space-y-5">
              <div className="flex items-center justify-between gap-2 pb-3 border-b border-slate-200">
                <div className="flex items-center gap-2">
                  <Sliders className="w-4 h-4 text-[#2D78FF]" aria-hidden="true" />
                  <span className="text-sm font-bold text-[#0B1B3D]">
                    {lang === 'ar' ? 'لوحة التجربة والتحكم المباشر' : 'Live Interactive Parameter Deck'}
                  </span>
                </div>
                <span className="text-xs font-mono text-slate-500 tabular-nums ltr-inline">
                  {stage.gradeCode}
                </span>
              </div>

              {/* Dynamic Interactive Controls for Selected Stage */}
              {stage.id <= 2 && (
                <div className="space-y-4">
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'قوة الدفع (نيوتن)' : 'Push Force (N)'}</span>
                      <span className="font-mono tabular-nums font-bold">{pushForce} N</span>
                    </div>
                    <input
                      type="range"
                      min={1}
                      max={15}
                      value={pushForce}
                      onChange={(e) => setPushForce(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'زاوية ميل المسار (درجة)' : 'Ramp Incline Angle (°)'}</span>
                      <span className="font-mono tabular-nums font-bold">{inclineAngle}°</span>
                    </div>
                    <input
                      type="range"
                      min={0}
                      max={30}
                      value={inclineAngle}
                      onChange={(e) => setInclineAngle(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <div className="p-3 bg-slate-50 border border-slate-200 rounded text-xs space-y-1">
                    <div className="font-bold text-[#0B1B3D] tabular-nums">
                      {lang === 'ar'
                        ? `المسافة التقديرية المقطوعة: ${travelDistanceCm} سم`
                        : `Simulated Travel Distance: ${travelDistanceCm} cm`}
                    </div>
                    <p className="text-slate-600">
                      {lang === 'ar'
                        ? 'مفهوم العلوم والرياضيات: كلما زاد الميل أو الاحتكاك احتاجت العربة لقوة دفع أكبر.'
                        : 'Science & Math link: Steeper incline & friction reduce travel distance for fixed push.'}
                    </p>
                  </div>
                </div>
              )}

              {stage.id === 3 && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between p-3 bg-slate-50 border border-slate-200 rounded">
                    <div>
                      <div className="text-xs font-bold text-[#0B1B3D]">
                        {lang === 'ar' ? 'حالة مفتاح الدارة الآمنة (5V)' : 'Safe 5V Circuit Switch'}
                      </div>
                      <div className="text-xs text-slate-600">
                        {circuitClosed
                          ? lang === 'ar'
                            ? 'مغلقة — LED مضاء مع مقاومة حماية'
                            : 'Closed — LED lit via protective resistor'
                          : lang === 'ar'
                          ? 'مفتوحة — تم فصل الطاقة للتعديل الآمن'
                          : 'Open — Power disconnected for safe wiring'}
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={() => setCircuitClosed((p) => !p)}
                      className={`px-3 py-1.5 text-xs font-bold rounded transition-colors ${
                        circuitClosed
                          ? 'bg-[#059669] text-white'
                          : 'bg-slate-200 text-slate-800'
                      }`}
                    >
                      {circuitClosed
                        ? lang === 'ar'
                          ? 'مغلق (ON)'
                          : 'CLOSED'
                        : lang === 'ar'
                        ? 'مفتوح (OFF)'
                        : 'OPEN'}
                    </button>
                  </div>

                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'قيمة التوفير في المعادلة الحسابية' : 'Water-Saving Equation Addend'}</span>
                      <span className="font-mono tabular-nums font-bold">{ledBonus}</span>
                    </div>
                    <input
                      type="range"
                      min={1}
                      max={10}
                      value={ledBonus}
                      onChange={(e) => setLedBonus(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>

                  <div className="p-3 bg-slate-50 border border-slate-200 rounded text-xs font-mono tabular-nums">
                    {lang === 'ar'
                      ? `معادلة الصف الثالث: حالة LED (${circuitClosed ? 1 : 0}) + قيمة التوفير (${ledBonus}) = ${
                          (circuitClosed ? 1 : 0) + ledBonus
                        }`
                      : `G3 Math Equation: LED_State(${circuitClosed ? 1 : 0}) + Saving(${ledBonus}) = ${
                          (circuitClosed ? 1 : 0) + ledBonus
                        }`}
                  </div>
                </div>
              )}

              {stage.id === 4 && (
                <div className="space-y-4">
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'المسافة أمام الحساس (سم)' : 'Distance Ahead (cm)'}</span>
                      <span className="font-mono tabular-nums font-bold">{obstacleDist} cm</span>
                    </div>
                    <input
                      type="range"
                      min={5}
                      max={60}
                      value={obstacleDist}
                      onChange={(e) => setObstacleDist(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <div className="p-3 bg-[#0B1B3D] text-white rounded font-mono text-xs space-y-1 ltr-inline text-start">
                    <div className="text-[#E2C258]">// PictoBlox / Block Logic</div>
                    <div>if (distance &lt; 20 cm) &#123; stop_cart(); alert_LED(ON); &#125;</div>
                    <div>else &#123; drive_forward(); &#125;</div>
                    <div className="pt-1 text-emerald-300 font-bold">
                      &gt; Result: {obstacleDist < 20 ? 'STOP & ALERT TRIGGERED' : 'CLEAR — DRIVING FORWARD'}
                    </div>
                  </div>
                </div>
              )}

              {stage.id === 5 && (
                <div className="space-y-4">
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'قراءة حساس HC-SR04 (سم)' : 'HC-SR04 Distance Reading (cm)'}</span>
                      <span className="font-mono tabular-nums font-bold">{sensorDistance} cm</span>
                    </div>
                    <input
                      type="range"
                      min={5}
                      max={90}
                      value={sensorDistance}
                      onChange={(e) => setSensorDistance(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>

                  <div className="flex items-center gap-2">
                    <button
                      type="button"
                      onClick={handleLogReading}
                      className="inline-flex items-center gap-1.5 px-3 py-2 text-xs font-bold bg-[#2D78FF] text-white rounded hover:bg-[#1E60D5] transition-colors"
                    >
                      <Plus className="w-3.5 h-3.5" />
                      <span>{lang === 'ar' ? 'تسجيل عينة في الجدول' : 'Log Trial Reading'}</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => setSampleReadings([])}
                      className="inline-flex items-center gap-1 px-3 py-2 text-xs font-medium bg-slate-100 text-slate-700 rounded hover:bg-slate-200 transition-colors"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                      <span>{lang === 'ar' ? 'تصفير' : 'Reset'}</span>
                    </button>
                  </div>

                  {/* Mini Time-Series Sparkline + Mean & Range */}
                  <div className="p-3 bg-slate-50 border border-slate-200 rounded space-y-2">
                    <div className="flex items-center justify-between text-xs font-mono tabular-nums">
                      <span>
                        {lang === 'ar' ? `العينات: ${sampleReadings.length}/10` : `Samples: ${sampleReadings.length}/10`}
                      </span>
                      <span className="font-bold text-[#0B1B3D]">
                        {lang === 'ar'
                          ? `المتوسط: ${g6Stats.mean} سم · المدى: ${g6Stats.range}`
                          : `Mean: ${g6Stats.mean} cm · Range: ${g6Stats.range}`}
                      </span>
                    </div>
                    {sampleReadings.length > 0 && (
                      <div className="flex items-end gap-1.5 h-14 pt-2">
                        {sampleReadings.map((val, idx) => (
                          <div
                            key={idx}
                            className="flex-1 bg-[#2D78FF] rounded-t transition-all duration-150"
                            style={{ height: `${Math.max(12, Math.round((val / 90) * 100))}%` }}
                            title={`${val} cm`}
                          />
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              )}

              {stage.id === 6 && (
                <div className="space-y-4">
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'إشارة تحكم L298N (PWM %)' : 'L298N Motor PWM Duty (%)'}</span>
                      <span className="font-mono tabular-nums font-bold">{pwmDuty}%</span>
                    </div>
                    <input
                      type="range"
                      min={0}
                      max={100}
                      value={pwmDuty}
                      onChange={(e) => setPwmDuty(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'مستوى الخزان المستهدف (%)' : 'Closed-Loop Tank Target (%)'}</span>
                      <span className="font-mono tabular-nums font-bold">{tankTarget}%</span>
                    </div>
                    <input
                      type="range"
                      min={15}
                      max={95}
                      value={tankTarget}
                      onChange={(e) => setTankTarget(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <div className="grid grid-cols-2 gap-2 text-xs font-mono tabular-nums">
                    <div className="p-2.5 bg-slate-50 border border-slate-200 rounded">
                      <div className="text-slate-500">{lang === 'ar' ? 'معدل الضخ' : 'Pump Flow'}</div>
                      <div className="font-bold text-[#0B1B3D]">{pumpFlowLpm} L/min</div>
                    </div>
                    <div className="p-2.5 bg-slate-50 border border-slate-200 rounded">
                      <div className="text-slate-500">ACS712 Current</div>
                      <div className="font-bold text-[#0B1B3D]">{motorCurrentMa} mA</div>
                    </div>
                  </div>
                </div>
              )}

              {stage.id === 7 && (
                <div className="space-y-4">
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'السماحية الميكانيكية في CAD (±mm)' : 'CAD Mechanical Tolerance (±mm)'}</span>
                      <span className="font-mono tabular-nums font-bold">±{cadTolerance} mm</span>
                    </div>
                    <input
                      type="range"
                      min={0.1}
                      max={2.0}
                      step={0.1}
                      value={cadTolerance}
                      onChange={(e) => setCadTolerance(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <div className="p-3 bg-slate-50 border border-slate-200 rounded text-xs space-y-1.5">
                    <div className="font-bold text-[#0B1B3D]">
                      {cadTolerance <= 0.8
                        ? lang === 'ar'
                          ? 'نتيجة المحاكاة في Wokwi/CAD: مطابقة لمعيار القبول'
                          : 'CAD / Wokwi Verification: PASS Acceptance Spec'
                        : lang === 'ar'
                        ? 'تنبيه محاكاة: السماحية مرتفعة — يُخشى تسريب الصمام'
                        : 'Simulation Warning: Loose tolerance risks valve leak'}
                    </div>
                    <p className="text-slate-600">
                      {lang === 'ar'
                        ? 'يجب توثيق فشل افتراضي واحد وتعديله قبل استلام مواد التنفيذ.'
                        : 'Student logs 1 virtual failure and revises design before procurement.'}
                    </p>
                  </div>
                </div>
              )}

              {stage.id === 8 && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between p-3 bg-slate-50 border border-slate-200 rounded">
                    <div className="text-xs">
                      <div className="font-bold text-[#0B1B3D]">ESP32 MQTT Telemetry Stream</div>
                      <div className="text-slate-500 font-mono">Topic: gis/obour/waterbot</div>
                    </div>
                    <button
                      type="button"
                      onClick={() => setMqttLive((p) => !p)}
                      className={`px-3 py-1.5 text-xs font-bold rounded ${
                        mqttLive ? 'bg-[#2D78FF] text-white' : 'bg-slate-200 text-slate-800'
                      }`}
                    >
                      {mqttLive ? (lang === 'ar' ? 'بث نشط' : 'ACTIVE') : (lang === 'ar' ? 'متوقف' : 'PAUSED')}
                    </button>
                  </div>
                  <label className="block space-y-1.5">
                    <div className="flex justify-between text-xs font-medium text-slate-700">
                      <span>{lang === 'ar' ? 'القيمة المرسلة للوحة Node-RED' : 'Published Tank Payload (%)'}</span>
                      <span className="font-mono tabular-nums font-bold">{tankTarget}%</span>
                    </div>
                    <input
                      type="range"
                      min={15}
                      max={95}
                      value={tankTarget}
                      onChange={(e) => setTankTarget(Number(e.target.value))}
                      className="w-full accent-[#2D78FF]"
                    />
                  </label>
                  <div className="p-3 bg-[#0B1B3D] text-emerald-300 font-mono text-xs rounded ltr-inline text-start">
                    &#123; "node": "ESP32_G11", "level_pct": {tankTarget}, "status": "{tankTarget < 25 ? 'LOW_ALERT' : 'NOMINAL'}", "keys_exposed": false &#125;
                  </div>
                </div>
              )}

              {stage.id === 9 && (
                <div className="space-y-3">
                  <div className="text-xs font-bold text-[#0B1B3D]">
                    {lang === 'ar'
                      ? 'حاسبة Rubric التقييم المزدوج لمشروع التخرج (من 100):'
                      : 'Dual-Evaluation G12 Capstone 4D Rubric Calculator:'}
                  </div>
                  {(
                    [
                      { key: 'design', ar: 'التصميم الهندسي', en: 'Engineering Design' },
                      { key: 'build', ar: 'جودة البناء والسلامة', en: 'Build & Safety' },
                      { key: 'code', ar: 'البرمجة والتكامل', en: 'Code & Integration' },
                      { key: 'docs', ar: 'التوثيق والدفاع النقدي', en: 'Docs & Defense' },
                    ] as const
                  ).map((dim) => (
                    <label key={dim.key} className="block space-y-1">
                      <div className="flex justify-between text-xs text-slate-700">
                        <span>{lang === 'ar' ? dim.ar : dim.en}</span>
                        <span className="font-mono tabular-nums font-bold">{rubricScores[dim.key]}/25</span>
                      </div>
                      <input
                        type="range"
                        min={5}
                        max={25}
                        value={rubricScores[dim.key]}
                        onChange={(e) =>
                          setRubricScores((prev) => ({ ...prev, [dim.key]: Number(e.target.value) }))
                        }
                        className="w-full accent-[#0B1B3D]"
                      />
                    </label>
                  ))}
                  <div className="p-3 bg-[#0B1B3D] text-white rounded flex items-center justify-between text-xs">
                    <span>{lang === 'ar' ? 'المستوى المحقق:' : 'Achieved Level:'}</span>
                    <span className="font-bold text-[#D4AF37] tabular-nums">
                      {totalRubric}/100 · {rubricTier[lang]}
                    </span>
                  </div>
                </div>
              )}
            </div>

            {/* Active Format Adaptation Callout */}
            <div className="p-4 bg-[#FBF9F4] border border-slate-200 rounded space-y-1.5">
              <div className="text-xs font-bold text-[#0B1B3D]">
                {lang === 'ar'
                  ? 'تطبيق هذه المرحلة في الصيغة المختارة:'
                  : 'Delivery Format Adaptation:'}
              </div>
              <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
                {stage.formatAdaptations[schoolFormat][lang]}
              </p>
            </div>
          </div>
        </div>

        {/* 4-Column Detailed Stage Specification Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {/* 1. Output & Added Layer */}
          <div className="bg-white border border-slate-200 rounded p-5 space-y-4">
            <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
              <Activity className="w-4 h-4 text-[#2D78FF]" aria-hidden="true" />
              <span>{lang === 'ar' ? 'الناتج والتراكم المعرفي' : 'Output & Added Layer'}</span>
            </div>
            <div className="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
              <div>
                <span className="font-bold text-[#0B1B3D] block mb-0.5">
                  {lang === 'ar' ? 'الناتج السنوي:' : 'Student Deliverable:'}
                </span>
                {stage.studentOutput[lang]}
              </div>
              <div className="pt-2 border-t border-slate-100">
                <span className="font-bold text-[#2D78FF] block mb-0.5">
                  {lang === 'ar' ? 'ما يُضاف عن العام السابق:' : 'Added vs Prior Year:'}
                </span>
                {stage.addedLayer[lang]}
              </div>
              <ul className="pt-2 border-t border-slate-100 space-y-1 list-disc list-inside text-xs text-slate-600">
                {stage.skills.map((sk, idx) => (
                  <li key={idx}>{sk[lang]}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* 2. Curriculum Alignment */}
          <div className="bg-white border border-slate-200 rounded p-5 space-y-4">
            <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
              <BookOpen className="w-4 h-4 text-[#2D78FF]" aria-hidden="true" />
              <span>{lang === 'ar' ? 'الربط بالمناهج والتقييم' : 'Curriculum & Rubric'}</span>
            </div>
            <div className="space-y-2.5 text-xs sm:text-sm">
              {stage.curriculumLinks.map((lnk, idx) => (
                <div key={idx} className="pb-2 border-b border-slate-100 last:border-0 last:pb-0">
                  <div className="font-bold text-[#0B1B3D]">{lnk.subject[lang]}</div>
                  <div className="text-slate-600 text-xs leading-relaxed mt-0.5">
                    {lnk.connection[lang]}
                  </div>
                </div>
              ))}
              <div className="pt-2 border-t border-slate-200 text-xs text-slate-700">
                <span className="font-bold text-[#0B1B3D] block mb-0.5">
                  {lang === 'ar' ? 'أداة القياس:' : 'Assessment:'}
                </span>
                {stage.assessmentMethod[lang]}
              </div>
            </div>
          </div>

          {/* 3. Verified Reference BOM */}
          <div className="bg-white border border-slate-200 rounded p-5 space-y-4">
            <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
              <Cpu className="w-4 h-4 text-[#2D78FF]" aria-hidden="true" />
              <span>{lang === 'ar' ? 'المعدات والأسعار المرجعية' : 'Reference Kit & BOM'}</span>
            </div>
            <div className="space-y-3">
              {stage.bom.map((item, idx) => (
                <div key={idx} className="pb-2.5 border-b border-slate-100 last:border-0 last:pb-0 text-xs">
                  <div className="font-bold text-[#0B1B3D] ltr-inline text-start">{item.name}</div>
                  <div className="font-mono tabular-nums text-[#2D78FF] font-semibold mt-0.5">
                    {item.priceLabel[lang]}
                  </div>
                  <div className="text-slate-500 mt-0.5">{item.sourceNote[lang]}</div>
                </div>
              ))}
            </div>
            <div className="text-[11px] text-slate-500 pt-2 border-t border-slate-100 leading-relaxed">
              {lang === 'ar'
                ? 'المصدر المرجعي للقطع: electronicsegypt.com (تاريخ الاطلاع 28 أكتوبر 2026 — أسعار بداية تقديرية).'
                : 'Reference pricing: electronicsegypt.com (accessed 28 Oct 2026 — starting estimates only).'}
            </div>
          </div>

          {/* 4. Safety & Child Protection */}
          <div className="bg-white border border-slate-200 rounded p-5 space-y-4">
            <div className="flex items-center gap-2 text-sm font-bold text-[#0B1B3D]">
              <ShieldCheck className="w-4 h-4 text-[#059669]" aria-hidden="true" />
              <span>{lang === 'ar' ? 'ضوابط السلامة العمرية' : 'Age-Specific Safety'}</span>
            </div>
            <ul className="space-y-2.5 text-xs sm:text-sm text-slate-700">
              {stage.safetyRules.map((rule, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <AlertTriangle className="w-3.5 h-3.5 text-amber-600 shrink-0 mt-1" aria-hidden="true" />
                  <span className="leading-relaxed">{rule[lang]}</span>
                </li>
              ))}
            </ul>
            <div className="pt-2 border-t border-slate-100 text-[11px] text-slate-500 leading-relaxed">
              {lang === 'ar'
                ? 'المرجعية الإرشادية: UL 2054 · UL 1740 · IEC 62133-2 · موافقة ولي الأمر الكتابية تسبق أي تصوير.'
                : 'Guidance refs: UL 2054 · UL 1740 · IEC 62133-2 · Parental media consent mandatory.'}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
