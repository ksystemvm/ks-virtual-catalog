import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { LayoutMainComponent } from './layouts/layout-main/layout-main.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, LayoutMainComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend');
}
