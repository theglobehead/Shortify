import React from 'react';
import '../styles/info-form.css';

function InfoForm() {
  return (
    <div className="info-form">
        <label htmlFor="full-url">Full url:</label>
        <input type="text" id="full-url"/>
        <label htmlFor="short-url">Shortened url:</label>
        <div className="bottom-form">
            <input type="text" id="short-url"/>
            <div className="buttons">
                <button type="button" className="btn btn-warning">Clear</button>
                <button type="button" className="btn btn-secondary">Shorten</button>
            </div>
        </div>
    </div>
  );
}

export default InfoForm;
