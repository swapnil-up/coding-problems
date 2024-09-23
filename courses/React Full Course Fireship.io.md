

22-09-2024 08:48

Status:

Tags:



# React Full Course Fireship.io


### 01. React in 100 Seconds

JS library for building UI. Built by Facebook. Building components that represent logical resuable piece of code. Basically a js function.

The function returns a simple block of html. 

The syntax is written in JSX (how is typescript different?)

``` react 
function Item(props){
	return <p>{props.text}</p>
}
```

The parameter value when changed automatically changes the component argument.

```
import React, { useState } from 'react';

function Counter() {
  // Declare a state variable 'count' with an initial value of 0
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

export default Counter;

```

Some key libraries:
1. For static sites Gatsby
2. For server side rendering Next
3. For animation Spring
4. For forms Formik
5. For State Management Redux 

Easier to understand react native once you learn react. 


### 02. Anatomy

##### Using npx

npx create-react-app from cli to generate a template scaffold. This will generate a full React app with a folder structure, including `src`, `public`, and `node_modules`.

To then start the development server:
```
cd my-app
npm start
```
It handles the webpack config to combine all the js into a single file that can be used by the browser. 

package.json is where you install dependencies. The node_modules holds the source code for it. Do not touch

The public directory holds the static files and the html shell for your website. Within index we have a div with id "root" where the react code is mounted. No need to touch

index.js is where we work with the react components. It's our entrypoint. The reactDOM.render() takes an argument for the react app and the html element from the para above. We also import the global css which is the index.css

App.js is our bread and butter. A component and it's export is what is within. Rule of Thumb is that one component per file
```
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Hello World!</p>
      </header>
    </div>
  );
}

export default App;
```

for npm run build for production code.

when built all the js is stored into one file for the browser. The main is followed by a random hash to invalidate cache and see all changes. 
##### Using vite

```
npm create vite@latest my-vite-app
```
then choose framework React and variant Javascript. Then, 
```
cd my-vite-app
npm install
npm run dev
```

##### Using next.js

```
npx create-next-app@latest my-next-app
```

### 03. Components

We combine in a tree format. Such as 

```
App
 ├── Header
 │    ├── Navbar
 │    └── SearchBar
 ├── Main
 │    ├── Sidebar
 │    │    └── MenuItem
 │    └── Content
 │         ├── Article
 │         └── Comments
 └── Footer
```
Install react developer tools browser extension. Allows you to see how websites use react. Breaks down the component tree. 

We can create components with a simple function, an arrow function => or a class component.

```
class Hello extends Component { 
	render() { 
		return <h1>Hello, World!</h1>; 
	} 
} export default Hello;
```

You can create dynamic values in your code using {}. This can include change in state/ value like above or a calculation like {1+2+3}

A component once defined it can be used anywhere else. So a function MyComponent() could be called as <MyComponent />. Generally it starts as with a capital. You can also pass arguments as props.

```
function App() {
  return (
    <div>
      <Greeting name="Alice" />
    </div>
  );
}

export default App;

import React from 'react';

function Greeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}

export default Greeting;

```
Here the prop's value is a primitive but it can also be an object or another component. 
- for object bio={{age:75}}
- for component icon={<Logo />}

You can destructure a prop into parts with braces. So instead of props in the parameter we pass ({name, icon}), then we can write {icon} in the code instead of {props.icon}. 

The virtual dom allows quick re-rendering. 

A component can pass props from parent to child but not vice versa. data flow is only towards child. So best to make components small. 

Any component can project its inner HTML using {props.children}


###  04. Conditional Rendering

If need to choose between two completely different UIs just use if else statements.

Else if you wish to render some big UI like a wrapper then render a smaller UI within it. The { } means that it is a js expression, so we can't use if else statements, so we use a ternary operator. 'condition'?'true case':'false case'.

```
import React, { useState } from 'react';

function WelcomeMessage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div>
      {isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign in.</h1>}
      <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
        {isLoggedIn ? 'Logout' : 'Login'}
      </button>
    </div>
  );
}

export default WelcomeMessage;

```

Else you may want to show the UI or show nothing, in which case after the condition we write && to make the component on the right visible. 

Be careful with empty string or 0 return false in JS. This is why many coders use ternary operator with the false condition showing null. 


### 05. Loops

To render a collection of items we can use loops. Since like above, JSX is an expression we can't just write a for loop. So we can use an array map

so if our input data is an array of fruits, then we make that into a map of item and index, that is then displayed as a list. We must write the key we get warnings. The key allows each unique item to be tracked, so that we can re-render the changed variable only. 
```
import React from 'react';

function ItemList() {
  const items = ['Apple', 'Banana', 'Orange', 'Grapes'];

  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}

export default ItemList;

```

In the above example we've used index to map the key but this will not optimize performance, only suppress the error. The better way is to have the input list have ids that we call within the map parameters within a curly bracket.


### 06. Events

A signal from a browser that an interaction has happened like a click, mouse movement or something else.

In js we'd addEventListener to an element in the DOM to run a function. In react it's the same.

```
import React, { useState } from 'react';

function ButtonClick() {
  const [message, setMessage] = useState('Hello!');

  // Event handler function
  const handleClick = () => {
    setMessage('Button Clicked!');
  };

  return (
    <div>
      <p>{message}</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}

export default ButtonClick;

```
If we had to pass additional arguments in the handler such as 
	const handleClick= (event, foo)
then the called location also works as:
```
button onClick={(e)=>handleClick(e,23)}>
```

You can also pass the handler as a prop within another function
```
// Parent Component (App.js)
import React, { useState } from 'react';
import ChildButton from './ChildButton';

function App() {
  const [message, setMessage] = useState('Hello from Parent!');

  // Event handler function
  const handleClick = () => {
    setMessage('Button in Child Clicked!');
  };

  return (
    <div>
      <p>{message}</p>
      {/* Passing the event handler as a prop */}
      <ChildButton onButtonClick={handleClick} />
    </div>
  );
}

export default App;

// Child Component (ChildButton.js)
import React from 'react';

function ChildButton(props) {
  return <button onClick={props.onButtonClick}>Click Me from Child</button>;
}

export default ChildButton;

```

# References

