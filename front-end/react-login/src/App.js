
import "bootstrap/dist/css/bootstrap.min.css"
import "./App.css"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Auth from "./Auth"
import Register from "./register"
function App() {
  return (

    <BrowserRouter>
    <Routes>
      <Route path="/auth" element={<Auth />} />
    </Routes>
  </BrowserRouter>,
  <BrowserRouter>
  <Routes>
    <Route path="/register" element={<Auth />} />
  </Routes>
</BrowserRouter>
  )
   
}

export default App