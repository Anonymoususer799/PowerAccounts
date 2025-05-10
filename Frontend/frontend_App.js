import React from 'react';
import FinancialReports from './components/FinancialReports';
import TaxCalculator from './components/TaxCalculator';
import CurrencyConverter from './components/CurrencyConverter';
import PDFGenerator from './components/PDFGenerator';
import TemplateManager from './components/TemplateManager';
import EmailSender from './components/EmailSender';

const App = () => {
  return (
    <div>
      <h1>PowerAccounts</h1>
      <FinancialReports />
      <TaxCalculator />
      <CurrencyConverter />
      <PDFGenerator />
      <TemplateManager />
      <EmailSender />
    </div>
  );
};

export default App;