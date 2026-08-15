import { ApplicationConfig, provideZonelessChangeDetection, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
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
    provideRouter(routes),
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

