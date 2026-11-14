import React, { useEffect, useState } from 'react';
import { Footer } from './components/Footer';
import { GovernanceCommand } from './components/GovernanceCommand';
import { HeroSection } from './components/HeroSection';
import { LaunchEventHub } from './components/LaunchEventHub';
import { ProjectScaleHub } from './components/ProjectScaleHub';
import { RobotJourneyExplorer } from './components/RobotJourneyExplorer';
import { TopBar } from './components/TopBar';
import type { AudienceLens, Lang } from './types';

export const App: React.FC = () => {
  const [lang, setLang] = useState<Lang>('ar');
  const [lens, setLens] = useState<AudienceLens>('executive');

  useEffect(() => {
    const html = document.documentElement;
    html.lang = lang;
    html.dir = lang === 'ar' ? 'rtl' : 'ltr';
  }, [lang]);

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F4] text-[#0B0F14]">
      <TopBar lang={lang} />
      <main className="flex-1">
        <HeroSection
          lang={lang}
          onToggleLang={setLang}
          lens={lens}
          onChangeLens={setLens}
        />
        <RobotJourneyExplorer lang={lang} />
        <ProjectScaleHub lang={lang} />
        <LaunchEventHub lang={lang} />
        <GovernanceCommand lang={lang} />
      </main>
      <Footer lang={lang} onToggleLang={setLang} />
    </div>
  );
};

export default App;
