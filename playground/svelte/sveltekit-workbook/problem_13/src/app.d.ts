declare global {
  namespace App {
    // TODO: add the Locals interface with user: { name: string; role: string } | null
    interface Locals {
      user: { name: string; role: string } | null;
    }
  }
}

export {};
