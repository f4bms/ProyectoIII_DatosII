import { Injectable } from '@angular/core';
import * as jose from 'jose';
import * as CryptoJS from 'crypto-js';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private publicKey: string = `-----BEGIN PUBLIC KEY-----
  MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA91WwrScmSzrZDmk6zWpQ
  kr53OK0ZTIg0T558LY5t8qFBbQpnfqjC4Gkb2lGkd0atij5mcztozPxTQH8Ayd7F
  DXYnPar5Cg4D5kLQ49jQLiwETYOUCqj0fI4V8SXmIRpUB1h0oQVfwekRVsdDn+t7
  p+RWnReF7tCQwhoFQYGluAnsBkewspdR3eKIsgRb5fEldD7NV+J81QRUwz53df2E
  LKYeIxPmMvs0uRIjcvJvR9q6a0N7pSbeMUGlno/K20gagRObf241qCi9RR5uCUn2
  AW6HKvMaA1nNWdoXQM61pEL2WTZzf9uqVZtRYrKek+XezpugIYK+CbJ69IOlDPdR
  TQIDAQAB
  -----END PUBLIC KEY-----`;
  

  constructor() { }

  async encryptData(data: any): Promise<string> {
    const _publicKey = await jose.importSPKI(this.publicKey, 'RSA-OAEP')
    const plaintext = JSON.stringify(data);

    
    const jwe = await new jose.CompactEncrypt(
      new TextEncoder().encode(plaintext)
    )
      .setProtectedHeader({ alg: 'RSA-OAEP', enc: 'A256GCM' })
      .encrypt(_publicKey)

    return jwe;
  }

  hashData(data: string): string {
    // Generar un hash SHA-256
    return CryptoJS.SHA256(data).toString(CryptoJS.enc.Hex);
  }


}
