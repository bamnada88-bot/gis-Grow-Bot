import type { EducationalStage } from '../types';

export const EDUCATIONAL_STAGES: EducationalStage[] = [
  {
    id: 1,
    gradeCode: 'KG1–KG2',
    title: {
      ar: 'الاستكشاف الحسي والبناء البسيط',
      en: 'Sensory Exploration & Simple Building',
    },
    ageRange: '4–6',
    platform: {
      ar: 'WhalesBot U20 Pro (برمجة بلا شاشة) / كتل بناء',
      en: 'WhalesBot U20 Pro (Screenless) / Building Blocks',
    },
    studentOutput: {
      ar: 'أول مركبة متحركة من كتل متعددة و«ملف حركة» مصوّر باليد',
      en: 'First multi-block moving vehicle & illustrated hand-drawn motion log',
    },
    addedLayer: {
      ar: 'الانتقال من التعرّف على الكتل والمحاور إلى التركيب والتوفيق وتبرير اختيار القطعة',
      en: 'Moving from block recognition to multi-piece assembly and justifying part choices',
    },
    skills: [
      { ar: 'السبب والنتيجة الحسية (أدفع فيتحرك)', en: 'Cause & sensory effect' },
      { ar: 'التصنيف (كبير/صغير، ثقيل/خفيف)', en: 'Classification (size & weight)' },
      { ar: 'تتبّع تسلسل من ثلاث خطوات بالبطاقات', en: 'Following a 3-step card sequence' },
      { ar: 'الالتزام بقواعد السلامة الأساسية في المختبر', en: 'Following foundational lab safety rules' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'التصنيف، العدّ، المقارنة، والجمع والطرح المبسط في KG2', en: 'Sorting, counting, comparison, and basic addition/subtraction' },
      },
      {
        subject: { ar: 'العلوم', en: 'Science' },
        connection: { ar: 'الحركة السببية، الدفع والسحب، وخصائص المادة', en: 'Causal motion, push/pull, and material properties' },
      },
      {
        subject: { ar: 'اللغة العربية والإنجليزية', en: 'Arabic & English' },
        connection: { ar: 'وصف الخطوات الثلاث شفوياً بكلمة «لأن…»', en: 'Verbal 3-step narration using "because..."' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'طقم WhalesBot U20 Pro بالبطاقات والقلم الضوئي دون شاشات',
        en: 'WhalesBot U20 Pro kit with coding cards & optical pen (zero screen time)',
      },
      public_lite: {
        ar: 'كتل خشبية وورق مقوى وبطاقات اتجاه مطبوعة محلياً (أنشطة بلا كهرباء)',
        en: 'Locally crafted wooden/cardboard blocks & printed direction cards (unplugged)',
      },
      community: {
        ar: 'مسارات أرضية تفاعلية في النوادي ومراكز الشباب بأدوات إعادة التدوير الآمنة',
        en: 'Floor-mat challenges in youth centers using safe recycled assembly kits',
      },
    },
    waterBotStep: {
      ar: 'مرحلة التأسيس: عربة أولية تتحرك بالدفع لاستكشاف المسافة والاحتكاك داخل ممر المدرسة',
      en: 'Foundation: Push-driven chassis exploring distance and surface friction along the classroom lane',
    },
    safetyRules: [
      { ar: 'لا تشغيل للبطارية خارج مقعد الشحن المخصص', en: 'Battery operated only inside sealed compartment' },
      { ar: 'شاحن البطارية بيد المعلم فقط', en: 'Teacher-only battery charging protocol' },
      { ar: 'تُمنع القطع الصغيرة الحادة أو أي أدوات قطع', en: 'No sharp parts or cutting tools permitted' },
    ],
    assessmentMethod: {
      ar: 'بطاقة «أستطيع أن…» أسبوعية + قائمة رصد من 5 بنود + عرض صفّي دقيقتين',
      en: 'Weekly "I can..." card + 5-item observation checklist + 2-min show-and-tell',
    },
    rubricSample: {
      emerging: { ar: 'يتبع خطوة واحدة بتوجيه مباشر', en: 'Follows 1 step with direct guidance' },
      developing: { ar: 'يكمل تسلسل 3 بطاقات بمساعدة لفظية', en: 'Completes 3-card sequence with prompts' },
      proficient: { ar: 'يشرح «لأن…» مرتين ويلتزم بالسلامة', en: 'Explains "because" twice & obeys safety' },
      innovating: { ar: 'يبرر اختيار قطعة بديلة لتحسين الاتزان', en: 'Justifies alternative part for stability' },
    },
    bom: [
      {
        name: 'WhalesBot U20 Pro (4+)',
        priceLabel: { ar: 'تقدير: ~24,596 ج.م (US$305 شامل الضريبة)', en: 'Estimate: ~24,596 EGP (US$305 incl. tax)' },
        sourceNote: { ar: 'store.whalesbot.ai + eg.shagoof.com (28 أكتوبر 2026)', en: 'store.whalesbot.ai + eg.shagoof.com (28 Oct 2026)' },
      },
      {
        name: 'Building Blocks Ref Set',
        priceLabel: { ar: 'تقدير: ~949 ج.م', en: 'Estimate: ~949 EGP' },
        sourceNote: { ar: 'bingo.eg — مرجع سوق (28 أكتوبر 2026)', en: 'bingo.eg — market ref (28 Oct 2026)' },
      },
    ],
  },
  {
    id: 2,
    gradeCode: 'G1–G2',
    title: {
      ar: 'الحركة والأشكال والآليات الأساسية',
      en: 'Motion, Shapes & Basic Mechanisms',
    },
    ageRange: '6–8',
    platform: {
      ar: 'LEGO Education WeDo 2.0',
      en: 'LEGO Education WeDo 2.0',
    },
    studentOutput: {
      ar: 'عربة بمحرّك تسير في خط محدد أو ذراع رافعة بمحور مع تبرير التركيب',
      en: 'Motorized line cart or axle lever arm with written 2-line justification',
    },
    addedLayer: {
      ar: 'الانتقال من الحركة العشوائية إلى الحركة المقصودة ثم المقارنة بين تركيبتين بمعيار',
      en: 'From random push motion to intentional gearing and comparing two mechanisms',
    },
    skills: [
      { ar: 'فهم التروس والمحاور ونقل الحركة', en: 'Gears, axles & motion transfer' },
      { ar: 'قياس المسافة والزمن بالوحدات', en: 'Measuring distance & time in units' },
      { ar: 'التناظر والتوازن الهيكلي', en: 'Symmetry & structural balance' },
      { ar: 'تبرير أفضلية تصميم على آخر', en: 'Evidence-based design comparison' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'المسافة والزمن والمقارنة العددية بين محاولتين', en: 'Distance, time, and numeric comparison across trials' },
      },
      {
        subject: { ar: 'العلوم', en: 'Science' },
        connection: { ar: 'القوة والاحتكاك وميل السطح وأثره على التوقف', en: 'Force, friction, incline angle, and stopping distance' },
      },
      {
        subject: { ar: 'الفنون واللغة', en: 'Arts & Language' },
        connection: { ar: 'رسم مخطط العربة ووصف خطوات مرقمة بالعربية والإنجليزية', en: 'Sketching assembly & numbered steps in Arabic/English' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'مجموعة LEGO Education WeDo 2.0 + حساس المسافة المدمج',
        en: 'LEGO Education WeDo 2.0 kit + integrated distance tilt/motion sensor',
      },
      public_lite: {
        ar: 'نموذج تروس كرتونية ومحاور خشبية + محرك تيار مستمر ببطارية مغلقة 3V',
        en: 'Cardboard gear sets, wooden axles & sealed 3V DC geared motor',
      },
      community: {
        ar: 'تحدي «العربة المتوازنة» في مجموعات ثنائية داخل نوادي العلوم',
        en: '"Balanced Cart" paired challenge in community science clubs',
      },
    },
    waterBotStep: {
      ar: 'G1: عربة بعجلة واحدة أو عجلتين تدور بالضغط لنقل كوب ماء تجريبي (مفهوم القوة والدفع)',
      en: 'G1: Simple push-wheel cart carrying a test water cup (force & push concept)',
    },
    safetyRules: [
      { ar: 'المحرك مقفل الحلقة ولا يُفك دون إشراف المعلم', en: 'Closed-housing motor; never disassembled by students' },
      { ar: 'إبعاد الأصابع عن المحاور والتروس أثناء الدوران', en: 'Keep fingers clear of rotating axles & gears' },
      { ar: 'منع أدوات القطع تماماً لهذه الفئة العمرية', en: 'Zero cutting tools allowed for ages 6–8' },
    ],
    assessmentMethod: {
      ar: 'ملف مصغّر (رسم + سطران) + بطاقة تحقق من 6 بنود + سؤال شفهي: لو غيّرنا التروس ماذا يحدث؟',
      en: 'Mini portfolio (sketch + 2 lines) + 6-item checklist + oral "what-if gear" prompt',
    },
    rubricSample: {
      emerging: { ar: 'يبني العربة بالمتابعة دون ربط التروس', en: 'Builds cart via guide without explaining gears' },
      developing: { ar: 'يصل لخط النهاية ويقيس المسافة', en: 'Completes track & records distance' },
      proficient: { ar: 'يفسر كيف انتقلت الحركة ويقارن سرعتين', en: 'Explains motion transfer & compares 2 speeds' },
      innovating: { ar: 'يعدّل نسبة التروس لتحقيق اتزان أفضل', en: 'Adjusts gear ratio to optimize stability' },
    },
    bom: [
      {
        name: 'LEGO Education WeDo 2.0',
        priceLabel: { ar: '[يحتاج عرض سعر — غير متاح بسعر منشور]', en: '[RFQ Required — no public retail price]' },
        sourceNote: { ar: 'يتطلب عرض سعر رسمي من المورّد المعتمد', en: 'Requires official vendor quotation' },
      },
    ],
  },
  {
    id: 3,
    gradeCode: 'G3',
    title: {
      ar: 'الدوائر الإلكترونية والتعرّف الآمن على المكونات',
      en: 'Safe Electronic Circuits & Component Discovery',
    },
    ageRange: '8–9',
    platform: {
      ar: 'micro:bit V2 + دوائر بسيطة آمنة 5V (LED / بزر / جرس)',
      en: 'micro:bit V2 + Safe 5V Simple Circuits (LED / Pushbutton / Buzzer)',
    },
    studentOutput: {
      ar: 'دارة عملية بمصدر وسلك وحمل ومفتاح تضيء LED أو تطلق تنبيهاً صوتياً',
      en: 'Working closed circuit (source, wire, load, switch) driving LED & buzzer alert',
    },
    addedLayer: {
      ar: 'الانتقال النوعي من الحركة الميكانيكية إلى الإشارة الكهربائية والقطبية',
      en: 'Leap from mechanical motion to electrical signal, polarity & resistor protection',
    },
    skills: [
      { ar: 'التمييز بين التوصيل السليم وحالة القصر', en: 'Distinguishing valid circuit vs short circuit' },
      { ar: 'فهم دور المقاومة في حماية مصباح LED', en: 'Role of resistor in protecting LED' },
      { ar: 'قراءة مخطط دارة مبسّط قبل التوصيل', en: 'Reading a schematic before wiring' },
      { ar: 'فصل مصدر الطاقة قبل تعديل أي سلك', en: 'Power-off before rewiring habit' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'العلوم', en: 'Science' },
        connection: { ar: 'الدارة الكهربائية المغلقة والمفتوحة وموصلية المواد', en: 'Open/closed electric circuits and material conductivity' },
      },
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'دخول إضاءة LED في معادلة حسابية تُحسب بالجمع والطرح', en: 'Integrating LED trigger states into addition/subtraction equations' },
      },
      {
        subject: { ar: 'التكنولوجيا', en: 'Technology' },
        connection: { ar: 'تتبع مدخل (زر) ← مخرج (ضوء/صوت) على لوحة التجارب', en: 'Tracing Input (button) -> Output (LED/buzzer) on breadboard' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'لوحة micro:bit V2 + لوحة خبز ومقاومات وأسلاك توصيل مأمونة 5V',
        en: 'micro:bit V2 + solderless breadboard, resistors, LEDs & jumper kit (5V)',
      },
      public_lite: {
        ar: 'بطاريات AA في حامل محمي + أسلاك بمشابك تمساح + LED ومقاومات من السوق المحلي',
        en: 'Protected AA battery holder + alligator clips + local LED & resistor pack',
      },
      community: {
        ar: 'حقيبة «دارتي الأولى» المتنقلة بجهد 3V–5V دون أي لحام',
        en: 'Portable "My First Circuit" 3V–5V solderless kit',
      },
    },
    waterBotStep: {
      ar: 'G3: إضافة مصباح LED تنبيهي للعربة يدخل في معادلة رقمية لحساب استهلاك النقاط بالجمع',
      en: 'G3: Adding an alert LED to the water cart tied to an addition-based water-score equation',
    },
    safetyRules: [
      { ar: 'لا لحام في هذه المرحلة إطلاقاً — لوحة تجارب فقط', en: 'ZERO soldering at Grade 3 — solderless breadboards only' },
      { ar: 'جهد تشغيل بحد أقصى 5V ومراجعة القطب قبل التشغيل', en: '5V maximum limit + visual polarity check before power-on' },
      { ar: 'فصل الطاقة إجباري قبل لمس أو نقل أي سلك', en: 'Mandatory power disconnect before changing any wire' },
    ],
    assessmentMethod: {
      ar: 'اختبار عملي لتركيب الدارة + بطاقة «ارسم الدارة» + سؤالان شفهيان',
      en: 'Practical circuit assembly test + "Draw the Circuit" card + 2 oral checks',
    },
    rubricSample: {
      emerging: { ar: 'يركب الدارة بمطابقة ألوان الأسلاك فقط', en: 'Assembles circuit only by matching wire colors' },
      developing: { ar: 'يشغل LED ويدرك وظيفة المفتاح', en: 'Lights LED and identifies switch role' },
      proficient: { ar: 'يفسر دور المقاومة ويميز حالة القصر', en: 'Explains resistor protection & detects shorts' },
      innovating: { ar: 'يصمم مسار اختيار بين تنبيه ضوئي وصوتي', en: 'Builds dual selector path for light/sound alert' },
    },
    bom: [
      {
        name: 'micro:bit V2 + Breadboard/LED Kit',
        priceLabel: { ar: '[يحتاج عرض سعر]', en: '[RFQ Required]' },
        sourceNote: { ar: 'بانتظار عروض الموردين', en: 'Awaiting supplier quotation' },
      },
      {
        name: 'Arduino Pro Mini ATmega328 5V (متقدم اختياري)',
        priceLabel: { ar: 'تقدير: 200 ج.م', en: 'Estimate: 200 EGP' },
        sourceNote: { ar: 'electronicsegypt.com (28 أكتوبر 2026)', en: 'electronicsegypt.com (28 Oct 2026)' },
      },
    ],
  },
  {
    id: 4,
    gradeCode: 'G4–G5',
    title: {
      ar: 'البرمجة المرئية وتصحيح الأخطاء',
      en: 'Visual Programming & Debugging',
    },
    ageRange: '9–11',
    platform: {
      ar: 'LEGO Spike Prime / micro:bit + PictoBlox',
      en: 'LEGO Spike Prime / micro:bit + PictoBlox',
    },
    studentOutput: {
      ar: 'برنامج من 20–30 تعليمة بتكرار وشرط + بطاقة «الكود الذي أصلحته» في ملف الإنجاز',
      en: '20–30 block program using loops & conditionals + "Code I Fixed" debugging card',
    },
    addedLayer: {
      ar: 'الانتقال من التنفيذ المباشر إلى كتابة قواعد السلوك (if/else) واكتشاف الأخطاء في G5',
      en: 'From direct triggers to conditional behavior rules (if/else) and systematic debugging in G5',
    },
    skills: [
      { ar: 'بناء الخوارزمية: تسلسل، تكرار، شرط، متغير', en: 'Algorithmic thinking: sequence, loop, branch, variable' },
      { ar: 'قراءة كود زميل وتشخيص سبب الخلل وتصحيحه', en: 'Reading peer code & isolating logic bugs' },
      { ar: 'العمل ضمن فريق بأدوار واضحة موثقة', en: 'Structured team roles & task logging' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'التكنولوجيا والبرمجة', en: 'ICT & Coding' },
        connection: { ar: 'البرمجة المرئية بالكتل، المتغيرات، ومبادئ تتبع الأخطاء', en: 'Block-based logic, variables, and bug isolation' },
      },
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'المتغيرات، المقارنات المنطقية (< و>)، وحساب المسافة والسرعة', en: 'Variables, inequalities (< / >), and speed/distance math' },
      },
      {
        subject: { ar: 'اللغة العربية والإنجليزية', en: 'Arabic & English' },
        connection: { ar: 'كتابة خطوات الخوارزمية ووصف الخلل وتصحيحه بدقة لغوية', en: 'Writing precise pseudocode and bug-fix explanations' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'مجموعات LEGO Spike Prime أو micro:bit عبر بيئة PictoBlox',
        en: 'LEGO Spike Prime or micro:bit programmed via PictoBlox',
      },
      public_lite: {
        ar: 'بيئة PictoBlox أو Scratch على أجهزة المعمل المدرسي + بطاقات تتبّع خوارزمي ورقية',
        en: 'PictoBlox/Scratch on school lab PCs paired with offline algorithm cards',
      },
      community: {
        ar: 'ورش «أصلح الكود» التفاعلية لتحضير طلاب 9–14 سنة لمسارات مثل FLL',
        en: 'Interactive "Fix the Bug" coding labs aligned with 9–14 age pathways',
      },
    },
    waterBotStep: {
      ar: 'G5: روبوت مزوّد بمنطق شرطي يكتشف العوائق أو انخفاض المسافة ويحسب السرعة رياضياً',
      en: 'G5: Conditional logic robot measuring path distance & calculating travel speed mathematically',
    },
    safetyRules: [
      { ar: 'شحن البطاريات في المقعد المخصص فقط', en: 'Charge batteries strictly on designated dock' },
      { ar: 'تثبيت أجزاء الهيكل قبل تشغيل أي مسار تلقائي', en: 'Inspect structural fasteners before autonomous runs' },
    ],
    assessmentMethod: {
      ar: 'Rubric مصغّر (تصميم/بناء/برمجة) + بطاقة «الكود الذي أصلحته»',
      en: 'Mini Rubric (Design/Build/Code) + "Bug I Fixed" portfolio artifact',
    },
    rubricSample: {
      emerging: { ar: 'ينسخ الكتل دون تعديل الشرط', en: 'Copies blocks without customizing conditions' },
      developing: { ar: 'يستخدم تكراراً وشرطاً لتحقيق مهمة واحدة', en: 'Uses loop & if/else for a single task' },
      proficient: { ar: 'يكتشف السطر المسبب للخلل في كود غيره ويصلحه', en: 'Locates & fixes faulty block in peer code' },
      innovating: { ar: 'يوظف متغيرات لضبط السلوك ذاتياً عبر عدة محاولات', en: 'Uses variables to tune behavior across runs' },
    },
    bom: [
      {
        name: 'LEGO Spike Prime / micro:bit V2 / PictoBlox',
        priceLabel: { ar: '[يحتاج عرض سعر]', en: '[RFQ Required]' },
        sourceNote: { ar: 'غير متاح بسعر موثق منشور', en: 'Awaiting verified vendor quotation' },
      },
      {
        name: 'NodeMCU ESP8266 ESP-12E (اختياري متقدم)',
        priceLabel: { ar: 'تقدير: 175 ج.م', en: 'Estimate: 175 EGP' },
        sourceNote: { ar: 'electronicsegypt.com (28 أكتوبر 2026)', en: 'electronicsegypt.com (28 Oct 2026)' },
      },
    ],
  },
  {
    id: 5,
    gradeCode: 'G6',
    isRecommendedPilot: true,
    title: {
      ar: 'الحساسات وجمع البيانات الكمية',
      en: 'Sensors & Quantitative Data Collection',
    },
    ageRange: '11–12',
    platform: {
      ar: 'Arduino Uno R3 + HC-SR04 / DHT22 / LM35DZ / MPU-6050',
      en: 'Arduino Uno R3 + HC-SR04 / DHT22 / LM35DZ / MPU-6050',
    },
    studentOutput: {
      ar: 'جهاز قياس ومعايرة يسجّل 10 قراءات ويحسب المتوسط والمدى مع رسم بياني زمني',
      en: 'Calibrated sensor station recording 10 trials with Mean, Range & time-series plot',
    },
    addedLayer: {
      ar: 'الانتقال من سؤال «هل يعمل؟» إلى سؤال «كم القيمة؟ وما هامش الخطأ؟» (نقطة التجربة الاستهلالية الموصى بها)',
      en: 'From "Does it work?" to "What is the exact measurement & error margin?" (Recommended Pilot Entry)',
    },
    skills: [
      { ar: 'المعايرة (Calibration) وقراءة المحوّل التناظري الرقمي ADC', en: 'Sensor calibration & ADC conversion' },
      { ar: 'تسجيل 10 عينات وحساب المتوسط الحسابي والمدى', en: '10-sample logging, mean & range analysis' },
      { ar: 'رسم البيانات زمنياً واستخلاص استنتاج علمي مكتوب', en: 'Time-series plotting & written inference' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'الإحصاء الوصفي: المتوسط الحسابي، المدى، والنسبة المئوية للخطأ', en: 'Descriptive statistics: Mean, Range, and % error' },
      },
      {
        subject: { ar: 'العلوم', en: 'Science' },
        connection: { ar: 'دقة أدوات القياس، تغيّر الحرارة والرطوبة والمسافة بالموجات الصوتية', en: 'Instrument precision, thermal/humidity tracking & ultrasonics' },
      },
      {
        subject: { ar: 'التكنولوجيا', en: 'Technology' },
        connection: { ar: 'ربط الحساس بـ Arduino Uno وقراءة Serial Monitor', en: 'Interfacing sensors with Arduino Uno & Serial Monitor' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'طقم Arduino Uno R3 كامل مع HC-SR04 وDHT22 وLM35DZ وMPU-6050',
        en: 'Full Arduino Uno R3 kit with HC-SR04, DHT22, LM35DZ & MPU-6050',
      },
      public_lite: {
        ar: 'مشاركة طقم Arduino Uno واحد لكل مجموعة (3–4 طلاب) مع حساس مسافة وحرارة محلي',
        en: 'Shared Arduino Uno kit per 3–4 students with core ultrasonic & temp sensors',
      },
      community: {
        ar: 'مختبر قياس ميداني لجودة البيئة الصفية وترشيد استهلاك المياه في الحي',
        en: 'Field measurement workshop tracking classroom climate & local water usage',
      },
    },
    waterBotStep: {
      ar: 'G6: حساس المسافة HC-SR04 يقيس ارتفاع سطح الماء في الخزان بدقة السنتيمتر ويحسب معدل الاستهلاك',
      en: 'G6: HC-SR04 ultrasonic sensor measures tank water height in cm across 10 logged trials',
    },
    safetyRules: [
      { ar: 'جهد تشغيل 5V و12V معزول فقط — يُمنع جهد الشبكة تماماً', en: 'Isolated 5V/12V only — mains voltage strictly prohibited' },
      { ar: 'طاولات عمل غير معدنية وفصل الطاقة قبل تعديل أي توصيل', en: 'Non-conductive workbenches & mandatory power-off before rewiring' },
    ],
    assessmentMethod: {
      ar: 'ورقة بيانات (10 قراءات + متوسط + مدى) + رسم بياني + سطر تفسير (ضمن EDU-05)',
      en: 'Data sheet (10 trials + mean + range) + chart + 1-line interpretation (EDU-05)',
    },
    rubricSample: {
      emerging: { ar: 'يسجل قراءات خام دون معايرة أو حساب متوسط', en: 'Logs raw values without calibration or mean' },
      developing: { ar: 'يحسب المتوسط والمدى لـ 10 قراءات', en: 'Computes mean & range for 10 readings' },
      proficient: { ar: 'يعاير الحساس ويفسر القيم الشاذة برسم بياني', en: 'Calibrates sensor & explains outliers via chart' },
      innovating: { ar: 'يقارن دقة حساسين ويحسب نسبة الخطأ المعياري', en: 'Benchmarks two sensors & computes error margin' },
    },
    bom: [
      {
        name: 'Arduino Uno R3 Compatible (ATmega328P)',
        priceLabel: { ar: 'تقدير: 239 ج.م', en: 'Estimate: 239 EGP' },
        sourceNote: { ar: 'electronicsegypt.com (28 أكتوبر 2026)', en: 'electronicsegypt.com (28 Oct 2026)' },
      },
      {
        name: 'LM35DZ Analog Temp Sensor',
        priceLabel: { ar: 'تقدير: 45 ج.م', en: 'Estimate: 45 EGP' },
        sourceNote: { ar: 'electronicsegypt.com (28 أكتوبر 2026)', en: 'electronicsegypt.com (28 Oct 2026)' },
      },
      {
        name: 'MPU-6050 GY-521 6-DOF IMU',
        priceLabel: { ar: 'تقدير: 110 ج.م', en: 'Estimate: 110 EGP' },
        sourceNote: { ar: 'electronicsegypt.com (28 أكتوبر 2026)', en: 'electronicsegypt.com (28 Oct 2026)' },
      },
      {
        name: 'HC-SR04 / DHT22 / Breadboard',
        priceLabel: { ar: '[يحتاج عرض سعر]', en: '[RFQ Required]' },
        sourceNote: { ar: 'بانتظار عرض سعر محدث', en: 'Awaiting updated quotation' },
      },
    ],
  },
  {
    id: 6,
    gradeCode: 'G7–G8',
    title: {
      ar: 'التحكم في الحركة وحلقات التغذية الراجعة',
      en: 'Actuation Control & Closed Feedback Loops',
    },
    ageRange: '12–14',
    platform: {
      ar: 'Arduino + سائقات L298N / ULN2003 + محركات MG995 / 28BYJ-48 + ACS712',
      en: 'Arduino + L298N / ULN2003 Drivers + MG995 / 28BYJ-48 + ACS712 Current Sensor',
    },
    studentOutput: {
      ar: 'نظام تحكم مغلق في G8 يضبط المضخة أو المحرك تلقائياً استناداً إلى قراءة الحساس وتيار التشغيل',
      en: 'Closed-loop feedback system in G8 auto-adjusting pump/actuator via sensor & current load',
    },
    addedLayer: {
      ar: 'الانتقال من حساس يقرأ فقط إلى نظام يتحكم بالحركة (G7) ثم حلقة تغذية راجعة مغلقة (G8)',
      en: 'From passive sensing to open actuation (G7) and self-correcting closed-loop control (G8)',
    },
    skills: [
      { ar: 'استخدام PWM لضبط السرعة وقراءة التيار عبر ACS712', en: 'PWM speed control & ACS712 current sensing' },
      { ar: 'اختيار سائق المحرك المناسب وتبرير العزم', en: 'Driver selection & torque justification' },
      { ar: 'بناء حلقة تغذية راجعة لضبط الاستقرار', en: 'Closed-loop feedback tuning for stability' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'العلوم', en: 'Science' },
        connection: { ar: 'الضغط، السيولة الهيدروليكية، العزم، والاتزان الفيزيائي', en: 'Pressure, fluid flow, torque, and equilibrium' },
      },
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'الدوال، التناسب العكسي بين السرعة والعزم، وحساب الطاقة', en: 'Functions, inverse speed/torque ratios, and power math' },
      },
      {
        subject: { ar: 'التكنولوجيا', en: 'Technology' },
        connection: { ar: 'إشارات PWM وبنية سائقات المحركات L298N وULN2003', en: 'PWM modulation and motor driver interfacing' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'طقم متكامل: Arduino + L298N + ULN2003 + MG995 + 28BYJ-48 + ACS712',
        en: 'Full kit: Arduino + L298N + ULN2003 + MG995 + 28BYJ-48 + ACS712',
      },
      public_lite: {
        ar: 'تركيز على وحدة L298N ومضخة 5V–12V مصغّرة مشتركة على مستوى مجموعات المختبر',
        en: 'Shared lab kits focusing on L298N driver & 5V–12V micro water pump',
      },
      community: {
        ar: 'ورشة تطبيقية: تحكّم آلي في صمام ري ذكي لنباتات النادي',
        en: 'Applied workshop: automated irrigation valve for club planter',
      },
    },
    waterBotStep: {
      ar: 'G7–G8: إضافة سائق L298N وخزان ومضخة صغيرة تُفتح وتُغلق تلقائياً حسب مستوى الماء وتيار الحمل',
      en: 'G7–G8: Adding L298N driver, reservoir & micro-pump with automatic closed-loop cutoff',
    },
    safetyRules: [
      { ar: 'حواجز حماية على الأجزاء المتحركة وزر فصل تيار فوري في متناول اليد', en: 'Physical guards on moving parts & reachable kill-switch' },
      { ar: 'منع تشغيل أي محرك غير مثبّت هيكلياً', en: 'Unsecured motors strictly prohibited from powering on' },
    ],
    assessmentMethod: {
      ar: 'اختبار أداء: 3 محاولات مقابل معايير قبول مكتوبة مسبقاً + توثيق التيار والاستهلاك',
      en: '3-run performance test against pre-written acceptance criteria + current log',
    },
    rubricSample: {
      emerging: { ar: 'يشغّل المحرك بسرعة ثابتة دون تحكم', en: 'Drives motor at constant speed without control' },
      developing: { ar: 'يضبط السرعة بـ PWM ويربطها بقراءة دخل', en: 'Adjusts speed via PWM linked to input' },
      proficient: { ar: 'يبني حلقة مغلقة توثّق التيار وتمنع الفيضان', en: 'Builds closed loop logging current & stopping overflow' },
      innovating: { ar: 'يوازن كفاءة التدفق مقابل استهلاك الطاقة', en: 'Optimizes flow efficiency against electrical draw' },
    },
    bom: [
      { name: 'ULN2003 Stepper Driver', priceLabel: { ar: 'تقدير: 25 ج.م', en: 'Estimate: 25 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: '28BYJ-48 5V Stepper', priceLabel: { ar: 'تقدير: 65 ج.م', en: 'Estimate: 65 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'TowerPro MG995 Servo', priceLabel: { ar: 'تقدير: 175 ج.م', en: 'Estimate: 175 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'ACS712 5A Current Sensor', priceLabel: { ar: 'تقدير: 80 ج.م', en: 'Estimate: 80 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'L298N Dual H-Bridge + Pump', priceLabel: { ar: '[يحتاج عرض سعر]', en: '[RFQ Required]' }, sourceNote: { ar: 'بانتظار عرض سعر محدث', en: 'Awaiting updated quotation' } },
    ],
  },
  {
    id: 7,
    gradeCode: 'G9–G10',
    title: {
      ar: 'التصميم الهندسي وإدارة المشروع قبل البناء',
      en: 'Engineering Design, Simulation & Project Governance',
    },
    ageRange: '14–16',
    platform: {
      ar: 'محاكاة Tinkercad / Wokwi + تصميم CAD + جدول BOM وإدارة المخاطر',
      en: 'Tinkercad / Wokwi Simulation + 2D/3D CAD + BOM & Risk Register',
    },
    studentOutput: {
      ar: 'نموذج رقمي مُختبَر بالمحاكاة + مخطط CAD بالسماحية + خطة تنفيذية وجدول ومخاطر (G10)',
      en: 'Simulated digital twin + CAD drawings with tolerances + G10 schedule/cost/risk plan',
    },
    addedLayer: {
      ar: 'التصميم والاختبار الافتراضي قبل التنفيذ المادي، ثم إضافة إدارة التكلفة والجدول في G10',
      en: 'Virtual verification before physical build (G9), adding BOM & schedule risk management (G10)',
    },
    skills: [
      { ar: 'تطبيق دورة التصميم الهندسي الكاملة وتوثيق الفشل الافتراضي', en: 'Full engineering design cycle & logging virtual failures' },
      { ar: 'صياغة 3 معايير قبول رقمية قابلة للقياس قبل البناء', en: 'Authoring 3 quantitative acceptance criteria pre-build' },
      { ar: 'تحليل قائمة المواد (BOM) وإدارة المخاطر والسماحية', en: 'BOM costing, mechanical tolerance & risk mitigation' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'الرياضيات', en: 'Mathematics' },
        connection: { ar: 'الهندسة الفراغية، السماحية (±mm)، وتقدير التكلفة والميزانية', en: 'Geometry, tolerance (±mm), and budget estimation' },
      },
      {
        subject: { ar: 'العلوم والهندسة', en: 'Science & Engineering' },
        connection: { ar: 'النمذجة الفيزيائية للتدفق والضغط الهيدروليكي قبل التجميع', en: 'Physical modeling of hydraulic flow before assembly' },
      },
      {
        subject: { ar: 'اللغة والمهارات الاجتماعية', en: 'Language & Life Skills' },
        connection: { ar: 'كتابة التقرير التقني وتوزيع الأدوار والالتزام بالجدول', en: 'Technical reporting, negotiation & schedule accountability' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'محاكاة Tinkercad/Wokwi + برامج CAD التعليمية + طباعة ثلاثية الأبعاد أو قطع أكريليك',
        en: 'Tinkercad/Wokwi + educational CAD suite + 3D-printed/laser-cut chassis',
      },
      public_lite: {
        ar: 'منصتا Tinkercad وWokwi المجانيتان على الويب + رسومات هندسية يدوية بمقياس رسم',
        en: 'Free web-based Tinkercad/Wokwi + scaled technical drafting on graph paper',
      },
      community: {
        ar: 'لجان مراجعة تصميم شبابية تعرض الفكرة افتراضياً قبل شراء أي مكوّن',
        en: 'Youth design review panels validating simulated prototypes prior to procurement',
      },
    },
    waterBotStep: {
      ar: 'G9–G10: تصميم المنظومة الهيدروليكية رقمياً واختبار سيناريوهات الفشل ووضع جدول BOM ومخاطر السلامة',
      en: 'G9–G10: Digital hydraulic layout in CAD/Wokwi + failure simulation + BOM & risk schedule',
    },
    safetyRules: [
      { ar: 'يُسمح باللحام بدءاً من G9 فقط: نظارة واقية، شفط أبخرة، لحام خالٍ من الرصاص، وبإشراف المعلم', en: 'Soldering begins G9+: goggles, fume extraction, lead-free solder, direct teacher supervision' },
      { ar: 'طاولات غير قابلة للاشتعال ومراجعة سلامة قبل كل جلسة', en: 'Non-flammable benches & mandatory pre-session safety check' },
    ],
    assessmentMethod: {
      ar: 'مراجعة تصميم شهرية أمام لجنة من معلمين + Rubric كامل + معايير القبول المكتوبة',
      en: 'Monthly design review before two-teacher panel + full Rubric + written acceptance specs',
    },
    rubricSample: {
      emerging: { ar: 'يبني مباشرة دون محاكاة أو معايير مسبقة', en: 'Builds directly without simulation or pre-specs' },
      developing: { ar: 'ينفذ محاكاة أساسية وجدول مواد مبدئي', en: 'Runs basic simulation & preliminary BOM' },
      proficient: { ar: 'يوثق فشلاً افتراضياً ويعدل التصميم مع خطرين وإجراءين', en: 'Logs virtual failure, revises CAD & maps 2 risks' },
      innovating: { ar: 'يقود مراجعة هندسية بميزانية محسوبة وسماحية دقيقة', en: 'Leads formal design review with tight tolerances & BOM' },
    },
    bom: [
      { name: 'Raspberry Pi Pico RP2040', priceLabel: { ar: 'تقدير: 550 ج.م', en: 'Estimate: 550 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'Arduino Uno R3 / NodeMCU', priceLabel: { ar: 'تقدير: 239 / 175 ج.م', en: 'Estimate: 239 / 175 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'Tinkercad / Wokwi / CAD (نسخ تعليمية)', priceLabel: { ar: '[يحتاج تأكيد — برمجيات مجانية]', en: '[Needs Confirmation — Free Edu Tier]' }, sourceNote: { ar: 'تحقق من سياسة الخصوصية وحسابات المدرسة', en: 'Verify school privacy & license terms' } },
    ],
  },
  {
    id: 8,
    gradeCode: 'G11',
    title: {
      ar: 'الأنظمة المتكاملة وإنترنت الأشياء (IoT)',
      en: 'Integrated Systems & IoT Telemetry',
    },
    ageRange: '16–17',
    platform: {
      ar: 'ESP32 WROOM-32 + MQTT / Node-RED + تطبيق MIT App Inventor',
      en: 'ESP32 WROOM-32 + MQTT / Node-RED + MIT App Inventor App',
    },
    studentOutput: {
      ar: 'نظام متصل يبث القراءات عبر Topic محدد إلى لوحة ويب حية وتطبيق هاتف مع تسجيل البيانات',
      en: 'Connected ESP32 system publishing live telemetry over MQTT to Node-RED dashboard & mobile app',
    },
    addedLayer: {
      ar: 'الانتقال من جهاز معزول داخل الغرفة إلى منظومة شبكية مترابطة تراعي أمن البيانات',
      en: 'From isolated bench device to networked telemetry system with foundational data security',
    },
    skills: [
      { ar: 'بنية النشر والاشتراك MQTT (Broker / Topic / Payload)', en: 'MQTT Publish-Subscribe architecture' },
      { ar: 'بناء لوحة Node-RED وتطبيق MIT App Inventor مع تسجيل Logging', en: 'Node-RED dashboard, mobile app & data logging' },
      { ar: 'تطبيق قواعد أمان أساسية وعدم كشف مفاتيح الاتصال على الإنترنت العام', en: 'Network security hygiene & credential protection' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'التكنولوجيا والشبكات', en: 'Technology & Networking' },
        connection: { ar: 'بروتوكولات Wi-Fi وMQTT والخوادم المحلية وبناء التطبيقات', en: 'Wi-Fi/MQTT protocols, local brokers, and mobile UI' },
      },
      {
        subject: { ar: 'الرياضيات والعلوم', en: 'Math & Science' },
        connection: { ar: 'تحليل السلاسل الزمنية والتمثيل البياني الفوري للقياس عن بُعد', en: 'Real-time time-series graphing and remote telemetry' },
      },
      {
        subject: { ar: 'اللغة الإنجليزية والعربية', en: 'English & Arabic' },
        connection: { ar: 'إعداد دليل التشغيل الفني وتوثيق بنية الرسائل', en: 'Technical operations manual & topic schema docs' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'وحدات ESP32 + شاشة OLED + قارئ RFID MFRC522 + خادم محلي Node-RED',
        en: 'ESP32 + OLED display + RFID MFRC522 + local Node-RED broker',
      },
      public_lite: {
        ar: 'ربط ESP32 بشبكة معمل محلية معزولة (Localhost Broker) دون حاجة لاشتراكات سحابية مدفوعة',
        en: 'Local isolated lab Wi-Fi & open-source broker (zero recurring cloud fees)',
      },
      community: {
        ar: 'مشروع رصد بيئي مشترك بين فرق الشباب يعرض قراءاته على لوحة موحدة',
        en: 'Shared youth civic telemetry dashboard aggregating local readings',
      },
    },
    waterBotStep: {
      ar: 'G11: وحدة ESP32 تنشر مستوى خزان المياه وحالة المضخة عبر MQTT إلى لوحة ويب حية وتنبيه عند العتبة',
      en: 'G11: ESP32 publishes live tank height & pump state over MQTT to web dashboard with threshold alerts',
    },
    safetyRules: [
      { ar: 'مرجع UL 60950-1: عدم لف البطارية داخل علبة مغلقة عديمة التهوية', en: 'UL 60950-1 ref: no sealed unventilated battery enclosures' },
      { ar: 'التيار المتردد (AC) خارج نطاق الطالب تماماً، ولا خادم مكشوف بمفاتيح عامة', en: 'AC mains strictly prohibited; zero exposed credentials on public web' },
    ],
    assessmentMethod: {
      ar: 'اختبار تشغيلي موثق (3 تشغيلات متتالية) + لقطات لوحة البيانات + مراجعة من زميل',
      en: '3 consecutive documented live telemetry runs + dashboard capture + peer review',
    },
    rubricSample: {
      emerging: { ar: 'يرسل قراءة غير منتظمة دون توثيق Topic', en: 'Transmits erratic payload without topic docs' },
      developing: { ar: 'يعرض القراءة على لوحة محلية مستقرة', en: 'Displays stable live reading on local dashboard' },
      proficient: { ar: 'يوثق رحلة البيانات كاملة ويطبّق قواعد عزل المفاتيح', en: 'Documents end-to-end data path & secures keys' },
      innovating: { ar: 'يدمج تنبيهات ثنائية وتطبيق هاتف بتسجيل تاريخي', en: 'Integrates dual alerts, mobile app & historical logs' },
    },
    bom: [
      { name: 'ESP32 WROOM-32 (CP2102)', priceLabel: { ar: 'تقدير: 280 ج.م', en: 'Estimate: 280 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: '1.3" I2C OLED 128×64', priceLabel: { ar: 'تقدير: 265 ج.م', en: 'Estimate: 265 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'RFID MFRC522 13.56 MHz', priceLabel: { ar: 'تقدير: 66.69 ج.م', en: 'Estimate: 66.69 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'SIM800L GSM/GPRS Module', priceLabel: { ar: 'تقدير: 275 ج.م', en: 'Estimate: 275 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
      { name: 'TCS3200 Color Sensor', priceLabel: { ar: 'تقدير: 260 ج.م', en: 'Estimate: 260 EGP' }, sourceNote: { ar: 'electronicsegypt.com (28 Oct 2026)', en: 'electronicsegypt.com (28 Oct 2026)' } },
    ],
  },
  {
    id: 9,
    gradeCode: 'G12',
    title: {
      ar: 'مشروع التخرج والتكامل الشامل',
      en: 'Capstone Graduation Project & Exhibition',
    },
    ageRange: '17–18',
    platform: {
      ar: 'تكامل تطبيقي شامل + ملف إنجاز تراكمي (KG–G12) + معرض وتقييم مزدوج',
      en: 'Full Integrated System + Cumulative Portfolio + External Exhibition',
    },
    studentOutput: {
      ar: 'منظومة متكاملة تحل مشكلة حقيقية + تقرير فني قابل للتكرار + عرض أمام لجنة داخلية وخارجية',
      en: 'Complete reproducible real-world system + technical report + dual-evaluated exhibition',
    },
    addedLayer: {
      ar: 'تجميع كل الطبقات الإحدى عشرة السابقة في منتَج موثق قابل للتكرار والتقييم المهني (دون ادعاء ضمان وظيفة أو قبول جامعي)',
      en: 'Synthesizing all prior layers into a reproducible, peer- & panel-defended product (no job/admission guarantees)',
    },
    skills: [
      { ar: 'تكامل الأنظمة (ميكانيكا + تحكم + بيانات + واجهة)', en: 'Full systems integration across hardware, control & software' },
      { ar: 'توثيق الفشل والقيود بصدق علمي إلى جانب النجاح', en: 'Transparent reporting of failures, limitations & evidence' },
      { ar: 'الدفاع العلمي عن قرارات التصميم أمام لجنة محكّمين', en: 'Defending design trade-offs before external reviewers' },
    ],
    curriculumLinks: [
      {
        subject: { ar: 'تكامل جميع المواد', en: 'Cross-Curricular Capstone' },
        connection: { ar: 'الرياضيات للتحليل الإحصائي، العلوم للتفسير، التكنولوجيا للتنفيذ، العربية والإنجليزية للتقرير والعرض', en: 'Math analysis, Science reasoning, Tech execution, Bilingual technical defense' },
      },
    ],
    formatAdaptations: {
      international: {
        ar: 'مشروع تخرج متكامل بمعرض سنوي ولجنة مراجعة أكاديمية وصناعية (بعد الاعتماد)',
        en: 'Full graduation system defended at annual showcase with invited external reviewers',
      },
      public_lite: {
        ar: 'مشروع تخرج مجتمعي بمكونات معاد استخدامها من سنوات المدرسة لحل مشكلة محلية',
        en: 'Low-cost community capstone built from cumulative reusable components',
      },
      community: {
        ar: 'معرض أقاليم مشترك يستعرض ملفات الإنجاز القابلة لإعادة البناء',
        en: 'Regional open showcase displaying reproducible student portfolios',
      },
    },
    waterBotStep: {
      ar: 'G12: نظام ترشيد مياه متكامل يعمل ميدانياً + تقرير هندسي بميزانية ومخاطر + ملف إنجاز يثبت التطور من KG إلى G12',
      en: 'G12: Complete field-ready water-conservation robot + technical dossier + full KG–G12 portfolio',
    },
    safetyRules: [
      { ar: 'خطة سلامة معرض كاملة: حواجز، نسخة احتياطية جاهزة، عدم وجود مصادر طاقة خطرة على المسرح', en: 'Full exhibition safety: barriers, verified backup unit, zero hazardous stage power' },
      { ar: 'موافقات تصوير كتابية قبل أي توثيق أو نشر إعلامي للطلاب', en: 'Written parental media consent mandatory prior to any photography/video' },
    ],
    assessmentMethod: {
      ar: 'تقييم مزدوج (معلم + مقيّم مستقل) عبر Rubric رباعي من 100 نقطة + مؤشر EDU-06 (هدف مبدئي ≥ 85% تسليم)',
      en: 'Dual evaluation (teacher + external reviewer) via 100-pt 4D Rubric + EDU-06 (provisional ≥ 85%)',
    },
    rubricSample: {
      emerging: { ar: 'نظام جزئي يفتقر للتكامل أو التوثيق', en: 'Partial system lacking integration or technical logs' },
      developing: { ar: 'يعمل في ظروف مضبوطة بتقرير وصفي أساسي', en: 'Operates in controlled run with descriptive report' },
      proficient: { ar: 'منظومة متكاملة مع اختبارات موثقة وقيود واضحة', en: 'Integrated system with verified tests & stated limits' },
      innovating: { ar: 'قابل للتكرار بالكامل من فريق آخر + دفاع نقدي متميز', en: 'Fully reproducible by peers + rigorous critical defense' },
    },
    bom: [
      { name: 'طقم المشروع التراكمي + قطع استبدال', priceLabel: { ar: '[يحتاج عرض سعر وفق BOM الطالب]', en: '[RFQ per student BOM]' }, sourceNote: { ar: 'يعتمد على BOM المعتمدة في G10', en: 'Based on approved G10 BOM' } },
    ],
  },
];
