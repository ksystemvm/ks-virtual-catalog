// frontend/src/app/features/catalog/components/catalog-list/catalog-list.component.ts
import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormControl } from '@angular/forms'; // <-- Importamos formularios
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

import { CatalogService } from '../../services/catalog.service';
import { ProductBase } from '../../models/catalog.models';

@Component({
  selector: 'app-catalog-list',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule], // <-- Añadimos ReactiveFormsModule aquí
  templateUrl: './catalog-list.component.html'
})
export class CatalogListComponent implements OnInit {
  private catalogService = inject(CatalogService);

  // --- ESTADOS DE DATOS ---
  products = signal<ProductBase[]>([]);
  loading = signal<boolean>(true);
  error = signal<string | null>(null);

  // --- ESTADOS DE PAGINACION ---
  currentPage = signal<number>(1);
  totalItems = signal<number>(0);
  totalPages = signal<number>(1);
  hasNext = signal<boolean>(false);
  hasPrevious = signal<boolean>(false);

  // Control de la barra de búsqueda
  searchControl = new FormControl('');

  constructor() {
    // Escuchamos lo que el usuario escribe en tiempo real
    this.searchControl.valueChanges.pipe(
      debounceTime(400), // Espera 400ms después de la última tecla presionada
      distinctUntilChanged(), // Solo busca si el texto es diferente al anterior
      takeUntilDestroyed() // Evita fugas de memoria cuando el componente se destruye
    ).subscribe(searchTerm => {
      this.currentPage.set(1);
      this.loadProducts(1, searchTerm || '');
    });
  }

  ngOnInit(): void {
    this.loadProducts(this.currentPage());
  }

  loadProducts(page: number, search: string = this.searchControl.value || ''): void {
    this.loading.set(true);
    this.error.set(null); 
    
    this.catalogService.getProducts(page, search).subscribe({
      next: (response) => {
        this.products.set(response.results);
        this.totalItems.set(response.count);

        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error al cargar el catálogo:', err);
        this.error.set('No se pudo conectar con el servidor. Verifica que Django esté corriendo.');
        this.loading.set(false);
      }
    });
  }
}