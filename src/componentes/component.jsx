import React, { useState } from 'react';

export default function Component() {
  const [text, settext] = useState('');
  const [updated, setupdated] = useState('');

  const textonchange = (event) => {
    settext(event.target.value);
  }

  const buttononClick = () => {
    setupdated(text);
  }
  return (
    <div>
      <input type="text" value={text} onChange={textonchange} />
      <button onClick={buttononClick}>send</button>
      <p>texto input: {text}</p>
      <p>actualizar</p>
      <p>texto actulizar: {updated}</p>
    </div>
  );
}
