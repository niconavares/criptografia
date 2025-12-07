from psec import tr31


def importar():
    """Importa y muestra información de un Key Block TR-31"""
    # Clave de transporte para desenvolver (unwrap) el bloque
    kbpk_b = bytes.fromhex("A1A10101010101010101010101010102")
    
    # Bloque TR31
    kb_string = "D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B"
    
    # Crear KeyBlock con el KBPK
    kb = tr31.KeyBlock(kbpk_b)
    
    # Cargar el header desde el Key Block string
    kb.header.load(kb_string)
    
    # Unwrappear la clave
    clave_unwrapped = kb.unwrap(kb_string)
    
    print("=" * 60)
    print("INFORMACIÓN DEL KEY BLOCK TR-31")
    print("=" * 60)
    print(f"Clave importada (hex):  {clave_unwrapped.hex().upper()}")
    print(f"Versión:                {kb.header.version_id}")
    print(f"Uso de clave:           {kb.header.key_usage}")
    print(f"Algoritmo:              {kb.header.algorithm}")
    print(f"Modo de uso:            {kb.header.mode_of_use}")
    print(f"Exportabilidad:         {kb.header.exportability}")
    print(f"Número de versión:      {kb.header.version_num}")
    print("=" * 60)


if __name__ == "__main__":
    importar()
