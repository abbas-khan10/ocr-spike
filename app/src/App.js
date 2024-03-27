import './App.scss';
import PdfViewer from "./PdfViewer";
import { Header, Button } from 'nhsuk-react-components';
import React from "react";

function App() {
  return (
      <div className="App">
        <Header>
          <Header.Container>
            <Header.Logo href="/" />
          </Header.Container>
        </Header>
        <main style={{marginLeft: 200}}><PdfViewer />
            <Button>Convert to text</Button>
            <div className="text-container" style={{ height: 600, width: 700}}></div>
        </main>
      </div>
  );
}

export default App;
