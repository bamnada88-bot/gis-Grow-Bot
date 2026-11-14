export type Lang = 'ar' | 'en';

export type AudienceLens = 'executive' | 'parent' | 'partner';

export type SchoolFormat = 'international' | 'public_lite' | 'community';

export interface BiText {
  ar: string;
  en: string;
}

export interface BomItem {
  name: string;
  priceLabel: BiText;
  sourceNote: BiText;
}

export interface CurriculumLink {
  subject: BiText;
  connection: BiText;
}

export interface EducationalStage {
  id: number;
  gradeCode: string;
  title: BiText;
  ageRange: string;
  isRecommendedPilot?: boolean;
  platform: BiText;
  studentOutput: BiText;
  addedLayer: BiText;
  skills: BiText[];
  curriculumLinks: CurriculumLink[];
  formatAdaptations: Record<SchoolFormat, BiText>;
  waterBotStep: BiText;
  safetyRules: BiText[];
  assessmentMethod: BiText;
  rubricSample: {
    emerging: BiText;
    developing: BiText;
    proficient: BiText;
    innovating: BiText;
  };
  bom: BomItem[];
}

export interface SupportPillar {
  id: number;
  title: BiText;
  principle: BiText;
  evidenceRequired: BiText;
  nationalContext: BiText;
}

export interface StakeholderItem {
  id: string;
  group: BiText;
  needsToSee: BiText;
  concerns: BiText;
  ourAsk: BiText;
  evidenceProvided: BiText;
}

export interface ProjectPhaseItem {
  code: string;
  title: BiText;
  timeframe: BiText;
  objectives: BiText;
  deliverables: string[];
  transitionGate: BiText;
  owner: BiText;
}

export interface RoadmapMilestone {
  id: string;
  period: BiText;
  phasesCovered: string;
  focus: BiText;
  gateType: 'Go / Adjust / Stop';
  gateCriteria: BiText;
}

export interface EventScheduleItem {
  time: string;
  duration: BiText;
  segment: BiText;
  category: 'setup' | 'gate' | 'plenary' | 'reception';
  goal: BiText;
  owner: string;
  output: BiText;
}

export interface DemoBeatItem {
  window: string;
  title: BiText;
  action: BiText;
  spokenCue: BiText;
}

export interface GoNoGoGate {
  id: number;
  time: string;
  title: BiText;
  owner: string;
  criteria: BiText;
  fallback: BiText;
}

export interface BudgetLineItem {
  id: number;
  name: BiText;
  basis: BiText;
  amount: number;
  unpricedWarning?: boolean;
}

export interface BudgetScenario {
  id: 'A' | 'B' | 'C';
  name: BiText;
  recommended?: boolean;
  invites: number;
  attendance: string;
  room: BiText;
  production: BiText;
  catering: BiText;
  contingencyRate: number;
  contingencyAmount: number;
  subtotal: number;
  floorTotal: number;
  unpricedBase: number;
  uncertaintyMargin25: number;
  ceilingTotal: number;
  items: BudgetLineItem[];
}

export interface PendingDecisionItem {
  id: number;
  title: BiText;
  owner: string;
  defaultIfPending: BiText;
  urgency: 'critical' | 'high' | 'standard';
}

export interface KpiItem {
  id: string;
  cluster: 'EVT' | 'EXE' | 'COM' | 'EDU';
  name: BiText;
  formula: BiText;
  owner: BiText;
  timing: BiText;
  baseline: BiText;
  provisionalTarget: BiText;
  levelNote?: string;
}

export interface RiskItem {
  id: string;
  title: BiText;
  likelihood: 'high' | 'medium' | 'low';
  impact: 'critical' | 'high' | 'medium';
  severity: 'critical' | 'high' | 'medium';
  owner: BiText;
  earlyWarning: BiText;
  prevention: BiText;
  response: BiText;
}
