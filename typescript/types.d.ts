export type AttestationSource =
  | 'EAS'
  | 'IcebreakerEAS'
  | 'Delegate_v1'
  | 'Delegate_v2'
  | 'Farcaster'
  | 'Jomo';

export type AttestationSchema = {
    id: string;
    name: string;
    source: AttestationSource;
    isOpen: boolean;
    allowRecursion: boolean;
    description?: string;
    schemaId?: string;
    chain?: string;
    schemaEncoding?: string;
    filter?: Record<string, string | boolean>;
    requiredSchemaName?: string;
    requiredFnames?: string[];
  };