import './App.css';
import axios from 'axios';

function test() {
  axios.get('/home').then((response) =>{
    console.log(response.data.home);
    }, (error) => {
      console.log(error);
    }); 
  }

function App() {
  return (
    <>
    <h1>
      Hello World;
    </h1>

    <button onClick={test}>
      Test this button
    </button>
    </>
  );
}

export default App;
