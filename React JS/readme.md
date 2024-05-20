- https://github.com/facebook/react
- React
  - single-page
  - server-rendered application
1. Install NodeJS (node -v)
2. Install create react app: npm install create-react-app
3. Create new project: create-react-app-project-name
4. Run project: npm start
5. main file: src/App.js

- React uses jsx: syntax extension to JavaScript. 
- eg. const element = <h1>Hello, world!</h1>;
- This funny tag syntax is neither a string nor HTML.It is called JSX, and it is a syntax extension to JavaScript.

- React uses virtual DOM to update in real time and then update the real DOM later.
- Virtual DOM vs real DOM: https://www.youtube.com/watch?v=RquK3TImY9U
  - React creates a copy of the real DOM called virtual DOM and check updates to it.
  - If there is an update to virtual DOM, React syncs this ***only this updated component*** to the real DOM thus saving time. 
