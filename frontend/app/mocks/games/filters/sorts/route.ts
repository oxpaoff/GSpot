import { generateMockFilterSortBy } from 'features/games'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(3)].map(() => generateMockFilterSortBy()))
}
