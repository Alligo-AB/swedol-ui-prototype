// HTTP basic auth for the whole docs site. Runs on Vercel before any file is served.
// Set DOCS_USER and DOCS_PASSWORD in Project → Settings → Environment Variables.
// If either is missing, the site stays open, so check the variables after setup.

export const config = { matcher: '/:path*' };

export default function middleware(request) {
  const user = process.env.DOCS_USER;
  const password = process.env.DOCS_PASSWORD;
  if (!user || !password) return undefined;

  const header = request.headers.get('authorization') || '';
  if (header.startsWith('Basic ')) {
    const [name, ...rest] = atob(header.slice(6)).split(':');
    if (name === user && rest.join(':') === password) return undefined;
  }

  return new Response('Authentication required', {
    status: 401,
    headers: { 'WWW-Authenticate': 'Basic realm="ECO Design System", charset="UTF-8"' },
  });
}
