import React, { useState } from 'react';
import './ToggleSwitch.css';


import ImageComponent from './ImageComponent'
import Defect_Area from './Defect_Area';

function ToggleSwitch() {
  const [showPageA, setShowPageA] = useState(true);

  const toggleToPageA = () => {
    setShowPageA(true);
  };

  const toggleToPageB = () => {
    setShowPageA(false);
  };

  return (
    <div className="toggle-switch-container">
      <div>
        <button
          className={`toggle-button ${showPageA ? 'active' : ''}`}
          onClick={toggleToPageA}
        >
          Defect Part Area
        </button>
        <button
          className={`toggle-button ${showPageA ? '' : 'active'}`}
          onClick={toggleToPageB}
        >
         Whole Field Area
        </button>
      </div>
      <div className="page-container">
        {showPageA ? <Defect_Area className="page" /> : <ImageComponent className="page" />}
      </div>
      
    </div>
  );
}

export default ToggleSwitch;
