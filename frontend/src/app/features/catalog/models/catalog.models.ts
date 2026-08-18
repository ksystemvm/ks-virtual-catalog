// --- INTERFACES BASE ---

export interface Unit {
  id: number;
  name: string;
}

export interface UnitDetail {
  id: number;
  unit: number;
  unitName: string;
  unitType: number;
  unitTypeDisplay: string;
  name: string;
  quantity: string; // Los DecimalField de Django llegan como strings en JSON
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  description: string | null;
  createdAt: string;
}

// --- VARIANTES E IMÁGENES ---

export interface VariantGroup {
  id: number;
  name: string;
}

export interface VariantGroupValue {
  id: number;
  group: number;
  groupName: string;
  value: string;
  htmlColor: string | null;
}

export interface ProductImage {
  id: number;
  image: string; // URL de la imagen que nos entrega el backend
  isMain: boolean;
  createdAt: string;
}

// --- PRODUCTOS (JERARQUÍA COMPLETA) ---

export interface Product {
  id: number;
  presentation: number;
  baseProductName: string;
  presentationName: string;
  variants: VariantGroupValue[];
  model: string | null;
  reference: string | null;
  extraPrice: string; // DecimalField desde Django
  totalPrice: string; // Propiedad calculada (@property)
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
  categoryName: string;
  name: string;
  slug: string;
  description: string | null;
  presentations: ProductPresentation[];
  createdAt: string;
  updatedAt: string;
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