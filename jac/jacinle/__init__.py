#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : __init__.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 01/18/2018
#
# This file is part of Jacinle.
# Distributed under terms of the MIT license.

from jac.jacinle.utils.init import init_main

init_main()

del init_main

from jac.jacinle.utils.env import jac_getenv, jac_is_verbose, jac_is_debug

if jac_getenv('IMPORT_ALL', 'true', 'bool'):
    from jac.jacinle.cli.argument import JacArgumentParser
    from jac.jacinle.cli.keyboard import yes_or_no, maybe_mkdir
    from jac.jacinle.cli.git import git_guard
    from jac.jacinle.concurrency.pool import TQDMPool
    from jac.jacinle.config.environ import load_env, has_env, get_env, set_env, with_env
    from jac.jacinle.logging.logger import get_logger, set_logger_output_file
    from jac.jacinle.utils.cache import cached_property, cached_result, fs_cached_result
    from jac.jacinle.utils.container import G, g, GView, SlotAttrObject, OrderedSet
    from jac.jacinle.utils.context import EmptyContext, KeyboardInterruptContext
    from jac.jacinle.utils.env import jac_getenv, jac_is_verbose, jac_is_debug
    from jac.jacinle.utils.debug import hook_exception_ipdb, exception_hook, timeout_ipdb, log_function, profile, time
    from jac.jacinle.utils.defaults import (
            defaults_manager, wrap_custom_as_default, gen_get_default, gen_set_default,
            option_context, FileOptions,
            default_args, ARGDEF
    )
    from jac.jacinle.utils.deprecated import deprecated
    from jac.jacinle.utils.enum import JacEnum
    from jac.jacinle.utils.env import jac_getenv, jac_is_debug, jac_is_verbose
    from jac.jacinle.utils.exception import format_exc
    from jac.jacinle.utils.imp import load_module, load_module_filename, load_source
    from jac.jacinle.utils.meta import (
            gofor,
            run_once, try_run,
            map_exec, filter_exec, first, first_n, stmap,
            method2func, map_exec_method,
            decorator_with_optional_args,
            cond_with, cond_with_group,
            merge_iterable,
            dict_deep_update, dict_deep_kv, dict_deep_keys,
            assert_instance, assert_none, assert_notnone,
            notnone_property, synchronized, timeout, Clock, make_dummy_func,
            repr_from_str
    )
    from jac.jacinle.utils.meter import GroupMeters
    from jac.jacinle.utils.naming import class_name, func_name, method_name, class_name_of_method
    from jac.jacinle.utils.network import get_local_addr
    from jac.jacinle.utils.numeric import safe_sum, mean, std, rms, prod, divup
    from jac.jacinle.utils.printing import indent_text, stprint, stformat, kvprint, kvformat, print_to_string, print_to, suppress_stdout
    from jac.jacinle.utils.tqdm import get_current_tqdm, tqdm, tqdm_pbar, tqdm_gofor, tqdm_zip
    from jac.jacinle.utils.uid import gen_time_string, gen_uuid4

    from jac.jacinle import io
    from jac.jacinle.io import load, dump
    from jac.jacinle import nd
    from jac.jacinle import random
    from jac.jacinle.random import reset_global_seed

    try:
        from IPython import embed
    except ImportError:
        pass

    try:
        from pprint import pprint
    except ImportError:
        pass

    JAC_VERBOSE = jac_is_verbose()
    JAC_DEBUG = jac_is_debug()

