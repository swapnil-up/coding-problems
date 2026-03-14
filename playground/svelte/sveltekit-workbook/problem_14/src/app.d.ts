declare global {
  namespace App {
    interface Locals {
      user: { name: string; role: string } | null;
    }
  }
}
export {};
