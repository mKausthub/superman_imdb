import React, { Suspense,useState } from "react";
import Routes from './components/Routes';
import Loader from './components/Loader/Loader';
function App() {
   return (
    <div>
    <Suspense fallback={<Loader />}>
      <Routes/>
    </Suspense>
    </div>
  );
}
export default App;
