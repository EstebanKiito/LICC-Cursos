import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Home } from './examples/Home'
import { UseCallbackExample } from './examples/UseCallbackExample'
import { UseEffectCleanupExample } from './examples/UseEffectCleanupExample'
import { UseTransitionExample } from './examples/UseTransitionExample'
import { CustomHooksExample } from './examples/CustomHooksExample'
import { CompositionExample } from './examples/CompositionExample'
import { HocExample } from './examples/HocExample'
import { ZustandExample } from './examples/ZustandExample'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/usecallback" element={<UseCallbackExample />} />
        <Route path="/useeffect-cleanup" element={<UseEffectCleanupExample />} />
        <Route path="/usetransition" element={<UseTransitionExample />} />
        <Route path="/custom-hooks" element={<CustomHooksExample />} />
        <Route path="/composition" element={<CompositionExample />} />
        <Route path="/hoc" element={<HocExample />} />
        <Route path="/zustand" element={<ZustandExample />} />
      </Routes>
    </BrowserRouter>
  )
}
