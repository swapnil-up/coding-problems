import { superValidate } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import type { PageServerLoad, Actions } from './$types';
import { loginSchema } from './schema';
import { fail } from "@sveltejs/kit";

export const load: PageServerLoad = async () => {
	const form = await superValidate(zod4(loginSchema));
	return { form };
};

export const actions: Actions = {
    default: async ({ request }) => {
        const form = await superValidate(request, zod4(loginSchema));

        if (!form.valid) {
            return fail(400, { form });
        }

        const { email, password } = form.data;
        
        if (email !== "admin@example.com" || password !== "password123") {
            return fail(401, { form, message: "Invalid credentials" });
        }

        return { form };
    }
};