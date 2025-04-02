```jsx
// App.jsx
import React from 'react';
import { atom, useAtom, useAtomValue, useSetAtom } from 'jotai';

// 🧪 Crear un átomo
const counterAtom = atom(0);

// 🧠 Leer y actualizar el átomo con useAtom
const Counter = () => {
  const [count, setCount] = useAtom(counterAtom);
  return (
    <div>
      <h2>Contador: {count}</h2>
      <button onClick={() => setCount((prev) => prev + 1)}>Incrementar</button>
    </div>
  );
};

// 👁️ Solo lectura con useAtomValue
const ReadOnlyCounter = () => {
  const count = useAtomValue(counterAtom);
  return <p>Contador actual: {count}</p>;
};

// ✍️ Solo escritura con useSetAtom
const ResetButton = () => {
  const setCount = useSetAtom(counterAtom);
  return <button onClick={() => setCount(0)}>Resetear</button>;
};

// 🧩 Composición de componentes
const App = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Ejemplo Jotai</h1>
      <Counter />
      <ReadOnlyCounter />
      <ResetButton />
    </div>
  );
};

export default App;
```
