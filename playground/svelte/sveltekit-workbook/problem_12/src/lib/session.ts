// Fake session store — in real apps use cookies or a DB
let loggedIn = false;
export const session = {
  isLoggedIn: () => loggedIn,
  login: () => { loggedIn = true; },
  logout: () => { loggedIn = false; },
};
