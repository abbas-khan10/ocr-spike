import './App.scss';
import PdfViewer from "./PdfViewer";
import { Header, Button } from 'nhsuk-react-components';
import React from "react";

function App() {
    const [data, setData] = React.useState({});

    async function extractText() {
      const response = await fetch("http://127.0.0.1:5000/extract");
      const res = await response.json();
      setData(res)
      console.log(res);
      console.log(res.time_taken);
    }

     React.useEffect(() => {
        extractText();
    }, [data]);

  return (
      <div className="App">
        <Header>
          <Header.Container>
            <Header.Logo href="/" />
          </Header.Container>
        </Header>
        <main style={{marginLeft: 200, marginTop: 100}}><PdfViewer />
            <Button onClick={extractText} style={{marginTop: 50}}>Convert to text</Button>
            <p>Time taken in seconds: {data.time_taken}</p>
            <div className="text-container" style={{ height: 600, width: 700, border: "1px solid black", marginBottom: 40}}>
                {data.response}
            </div>
        </main>
      </div>
  );
}

export default App;
