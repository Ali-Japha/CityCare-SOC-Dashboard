import { render, screen } from '@testing-library/react';
import App from './App';

test('renders CityCare Hospital header', () => {
  render(<App />);
  const headerElement = screen.getByText(/CityCare Hospital/i);
  expect(headerElement).toBeInTheDocument();
});
