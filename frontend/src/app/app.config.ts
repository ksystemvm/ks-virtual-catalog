import { ApplicationConfig, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter, withComponentInputBinding } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

import { provideIcons } from '@ng-icons/core';
import { 
  heroChevronLeft, heroChevronRight, heroSquares2x2, 
  heroCurrencyDollar, heroQueueList, heroGlobeAlt,
  heroArrowTrendingUp, heroPlus, heroCog6Tooth, heroCog,
} from '@ng-icons/heroicons/outline';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection(), 
    provideRouter(routes, withComponentInputBinding()),
    provideHttpClient(),
    provideIcons({
      heroChevronLeft, 
      heroChevronRight, 
      heroSquares2x2, 
      heroCurrencyDollar, 
      heroQueueList,
      heroGlobeAlt,
      heroArrowTrendingUp,
      heroPlus,
      heroCog,
      heroCog6Tooth,
    })
  ]
};

// import { ApplicationConfig, provideBrowserGlobalErrorListeners } from '@angular/core';
// import { provideRouter } from '@angular/router';

// import { routes } from './app.routes';

// export const appConfig: ApplicationConfig = {
//   providers: [
//     provideBrowserGlobalErrorListeners(),
//     provideRouter(routes)
//   ]
// };
