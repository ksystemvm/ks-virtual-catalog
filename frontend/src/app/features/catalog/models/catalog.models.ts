// --- INTERFACES BASE ---

export interface Unit {
  id: number;
  name: string;
}

export interface UnitDetail {
  id: number;
  unit: number;
  unit_name: string;
  unit_type: number;
  unit_type_display: string;
  name: string;
  quantity: string; 
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  description: string | null;
  created_at: string;
}

// --- VARIANTES E IMÁGENES ---

export interface VariantGroup {
  id: number;
  name: string;
}

export interface VariantGroupValue {
  id: number;
  group: number;
  group_name: string;
  value: string;
  html_color: string | null;
}

export interface ProductImage {
  id: number;
  image: string; // URL de la imagen que nos entrega el backend
  is_main: boolean;
  created_at: string;
}

// --- PRODUCTOS (JERARQUÍA COMPLETA) ---

export interface Product {
  id: number;
  presentation: number;
  base_product_name: string;
  presentation_name: string;
  variants: VariantGroupValue[];
  model: string | null;
  reference: string | null;
  extra_price: string; // DecimalField desde Django
  total_price: string; // Propiedad calculada (@property)
  stock: number;
  images: ProductImage[];
}

export interface ProductPresentation {
  id: number;
  product: number;
  unit: UnitDetail;
  price: string;
  products: Product[];
}

export interface ProductBase {
  id: number;
  category: number;
  category_name: string;
  name: string;
  slug: string;
  description: string | null;
  presentations: ProductPresentation[];
  created_at: string;
  updated_at: string;
}

// --- PAGINACIÓN GENÉRICA ---

/**
 * Interfaz genérica para manejar la respuesta paginada de Django REST Framework
 * (StandardResultsSetPagination).
 */
export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}