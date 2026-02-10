import { betterAuth } from "better-auth";
import { Pool } from "pg";

let dbUrl = process.env.DATABASE_URL;
if (dbUrl?.startsWith("postgresql+asyncpg://")) {
    dbUrl = dbUrl.replace("postgresql+asyncpg://", "postgresql://");
}

const pool = new Pool({
    connectionString: dbUrl,
    ssl: {
        rejectUnauthorized: false
    }
});

// @ts-ignore
export const auth: any = betterAuth({
    database: pool,
    emailAndPassword: {
        enabled: true
    },
});
