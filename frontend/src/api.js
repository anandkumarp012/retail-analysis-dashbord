const API_URL = (import.meta.env.VITE_API_URL || '').replace(/\/+$/, '');

export const withApiBase = (path) => {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return `${API_URL}${normalizedPath}`;
};

export default API_URL;
