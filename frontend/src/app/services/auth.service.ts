import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { jwtDecode } from 'jwt-decode';
import { tap } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private http = inject(HttpClient);
  private baseUrl = environment.apiUrl;

  private readonly APP_STORAGE_KEY = 'KS_VIRTUAL_CATALOG_ACCESS';

  login(credentials: {username: string; password: string}): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}login/`, credentials).pipe(
      tap(response => {
        if(response && response.access) {
          this.setToken(response.access);
        }
      })
    )
  }

  private getAppData(): any {
    const storedData = localStorage.getItem(this.APP_STORAGE_KEY);
    return storedData ? JSON.parse(storedData) : {};
  }

  setToken(token: string): void {
    const appData = this.getAppData();
    appData.access_token = token;
    localStorage.setItem(this.APP_STORAGE_KEY, JSON.stringify(appData));
  }
  
  getToken(): string | null {
    const appData = this.getAppData();
    return appData.access_token ? appData.access_token : null;
  }

  // Desencripta el token y extrae el rol que inyectamos en Django
  getUserRole(): string | null {
    const token = this.getToken();
    if (token) {
      try {
        const decodedToken: any = jwtDecode(token);
        return decodedToken.role || 'CUSTOMER';
      } catch (Error) {
        return null;
      }
    }
    return null;
  }

  register(payload: any): Observable<any> {
    return this.http.post(`${this.baseUrl}auth/register/`, payload);
  }

  activateAccount(uidb64: string, token: string): Observable<any> {
    return this.http.get(`${this.baseUrl}auth/activate/${uidb64}/${token}/`);
  }

  requestPasswordReset(email: string): Observable<any> {
    return this.http.post(`${this.baseUrl}auth/request-password-reset/`, { email });
  }

  resetPassword(payload: any): Observable<any> {
    return this.http.post(`${this.baseUrl}auth/reset-password/`, payload);
  }

  logout(): void {
    localStorage.removeItem(this.APP_STORAGE_KEY);
  }

  isLoggedIn(): boolean {
    return this.getToken() !== null;
  }



}