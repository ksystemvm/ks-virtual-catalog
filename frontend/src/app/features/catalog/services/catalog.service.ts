import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ProductBase, PaginatedResponse } from '../models/catalog.models';

@Injectable({
  providedIn: 'root'
})
export class CatalogService {
  // Ajusta el puerto o el prefijo de la URL si tu Django corre en otra dirección.
  // En un proyecto de producción, esto iría en un archivo de environment.
  private apiUrl = 'http://localhost:8000/api/catalog/products-base';

  constructor(private http: HttpClient) { }

  /**
   * Obtiene la lista de productos base de forma paginada.
   * Permite buscar por texto (nombre, descripción, etc.) si el backend lo soporta.
   */
  getProducts(page: number = 1, search: string = ''): Observable<PaginatedResponse<ProductBase>> {
    let params = new HttpParams().set('page', page.toString());
    
    if (search) {
      params = params.set('search', search);
    }

    return this.http.get<PaginatedResponse<ProductBase>>(this.apiUrl, { params });
  }

  /**
   * Obtiene el detalle completo de un producto base usando su ID o Slug.
   */
  getProductById(id: number | string): Observable<ProductBase> {
    return this.http.get<ProductBase>(`${this.apiUrl}/${id}/`);
  }
}